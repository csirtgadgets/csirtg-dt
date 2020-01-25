import arrow
from datetime import datetime
import re

RE_TS = re.compile(r'^(\d{4})-?(\d{2})-?(\d{2})[\s|T](\d{2})\:?(\d{2})\:?(\d{2})\s?(Z|\S{2,3}|[\+|\-]\d{2}\:\d{2})?$')


def _human_to_dt(ts):
    t = arrow.utcnow()

    if ts == 'now':
        return t

    if ts == 'hour':
        return t.replace(minute=0, second=0, microsecond=0)

    if ts == 'day':
        return t.replace(hour=0, minute=0, second=0, microsecond=0)

    if ts == 'week':
        return t.replace(day=7, hour=0, minute=0, second=0, microsecond=0)

    if ts == 'month':
        return t.replace(day=1, hour=0, minute=0, second=0, microsecond=0)


def _is_valid(ts):
    if isinstance(ts, arrow.Arrow):
        return ts

    t = _human_to_dt(ts)
    if t:
        return t

    try:
        t = arrow.get(ts)

    except Exception as e:
        return

    if t and t.year > 2000:
        return t


def _fudge_arrow(ts):
    t = None
    try:
        t = arrow.get(ts)

    except ValueError as e:
        match = RE_TS.search(ts)
        if match:
            ts = '{}-{}-{}T{}:{}:{}Z'.format(match.group(1), match.group(2),
                                             match.group(3), match.group(4),
                                             match.group(5), match.group(6))

            t = arrow.get(ts, 'YYYY-MM-DDTHH:mm:ssZ')
            return t

    except arrow.parser.ParserError as e:
        return

    if not t:
        return

    if t.year > 2000:
        return t

    if type(ts) == datetime:
        ts = str(ts)

    if len(ts) == 8:
        ts = '{}T00:00:00Z'.format(ts)
        t = arrow.get(ts, 'YYYYMMDDTHH:mm:ss')

    if t.year < 2000:
        return


def get(ts, fmt=None):
    if fmt:
        return arrow.get(ts, fmt)

    if isinstance(ts, datetime):
        return arrow.get(ts)

    try:
        match = re.search(r'^(\d{2})-(\d{2})-(\d{4})$', ts)
        if match:
            return f"{match.group(3)}-{match.group(2)}-{match.group(1)}T00:00:00Z"

    except Exception as e:
        pass

    try:
        t = arrow.get(ts)
        if t.year >= 2000:
            return t
    except Exception as e:
        pass

    valid = _is_valid(ts)
    if valid:
        return valid

    valid = _fudge_arrow(ts)
    if valid:
        return valid

    raise TypeError('Invalid Timestamp: %s' % ts)


def main():
    import sys

    ts = sys.argv[1]

    ts = get(ts)

    print(ts)


if __name__ == '__main__':
    main()
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
