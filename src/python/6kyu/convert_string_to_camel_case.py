def to_camel_case(text):
    return ''.join([
        word.capitalize() if index != 0 else word
        for index, word in enumerate(
            text.replace('-', ' ')
            .replace('_', ' ')
            .split(' ')
        )
    ])


def test_to_camel_case():
    assert to_camel_case('') == ''
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"
