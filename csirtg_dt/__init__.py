import arrow
from datetime import datetime
import re

from csirtg_dt.utils import _is_valid, _fudge_arrow, _human_to_dt


def get(ts, fmt=None):
    """Return an Arrow object from a timestamp

Examples:

    from csirtg_dt import get
    ts = get('20190101')
    ts = get('20190101', 'YYYYMMDD')

Arguments

    :param ts: timestamp string to parse
    :param fmt: optional (arrow) format string
    :return: arrow object
    """
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

