# CSIRTG-DT

A DateTime utility for security operators with a mission of doing the right thing.

# Examples

```bash
$ csirtg-dt 20190101
2019-01-01T00:00:00+00:00
```

```python
from csirtg_dt import get
from pprint import pprint

ts = get('20190101')
pprint(ts)
```