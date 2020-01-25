from csirtg_dt import get

TIMESTAMPS = {
    '2018-12-29 15:32:27 UTC',
    '2017-03-06T11:41:48-06:00',
    '20190101'
}


def test_timestamps():
    for t in TIMESTAMPS:
        assert get(t)


def test_human_dt():
    for e in ['now', 'hour', 'day', 'week', 'month']:
        assert get(e)
