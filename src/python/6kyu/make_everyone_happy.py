def smile(text):
    for eyes in (":", ";", "="):
        for nose in ("-", "~", ""):
            text = text.replace(eyes + nose + "(", eyes + nose + ")")
            text = text.replace(eyes + nose + "[", eyes + nose + "]")
    return text


def test_smile():
    assert smile('Howdy :(') == 'Howdy :)'
    assert smile('Never be sad =[') == 'Never be sad =]'
    assert smile(
        'It\'s been raining all day ;-(') == 'It\'s been raining all day ;-)'
    assert smile('My friend got married ;~[') == 'My friend got married ;~]'
    assert smile(
        'Change this `=(` and this `:[`') == 'Change this `=)` and this `:]`'
    assert smile(
        'Funny smileys: ;~[ :( :-( :~[ :-[') == 'Funny smileys: ;~] :) :-) :~] :-]'
    assert smile(
        'The list of positive numbers is [1,2,3,4...]') == 'The list of positive numbers is [1,2,3,4...]'
    assert smile('(((-)(((-)))(-)))') == '(((-)(((-)))(-)))'
