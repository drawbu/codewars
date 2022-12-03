# https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}"


def test_make_readable():
    # assert make_readable(0) == "00:00:00"
    assert make_readable(5) == "00:00:05"
    assert make_readable(60) == "00:01:00"
    assert make_readable(86399) == "23:59:59"
    assert make_readable(359999) == "99:59:59"
