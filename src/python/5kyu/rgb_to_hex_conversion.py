def rgb(r: int, g: int, b: int) -> str:
    hexa = lambda x: min(255, max(x, 0))
    return '{:02X}{:02X}{:02X}'.format(hexa(r), hexa(g), hexa(b))


def test_rgb():
    assert rgb(0, 0, 0) == "000000"
    assert rgb(1, 2, 3) == "010203"
    assert rgb(255, 255, 255) == "FFFFFF"
    assert rgb(254, 253, 252) == "FEFDFC"
    assert rgb(-20, 275, 125) == "00FF7D"
