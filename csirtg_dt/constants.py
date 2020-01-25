import re

from ._version import get_versions
VERSION = get_versions()['version']
del get_versions

RE_TS = re.compile(r'^(\d{4})-?(\d{2})-?(\d{2})[\s|T](\d{2})\:?(\d{2})\:?(\d{2})\s?(Z|\S{2,3}|[\+|\-]\d{2}\:\d{2})?$')
