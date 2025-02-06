from StringUtils import StringUtils


def test_reverse_string_positive():
    # positive
    assert StringUtils.reverse_string("Тест") == "тсеТ"
    assert StringUtils.reverse_string("123") == "321"
    assert StringUtils.reverse_string("04 апреля 2023") == \
        "40 ялерпа 3202"


def test_reverse_string_negative():
    # negative
    assert StringUtils.reverse_string("") == ""
    assert StringUtils.reverse_string(None) is None
    assert StringUtils.reverse_string(" ") == " "


def test_capitalize_string_positive():
    # positive
    assert StringUtils.capitalize_string("test") == "Test"
    assert StringUtils.capitalize_string("тест") == "Тест"
    assert StringUtils.capitalize_string("123abc") == "123abc"


def test_capitalize_string_negative():
    # negative
    assert StringUtils.capitalize_string("") == ""
    assert StringUtils.capitalize_string(None) is None
    assert StringUtils.capitalize_string(" ") == " "


def test_join_strings_positive():
    # positive
    assert StringUtils.join_strings(["Hello", "world"]) == "Hello world"
    assert StringUtils.join_strings(["04", "апреля", "2023"]) == \
        "04 апреля 2023"
    assert StringUtils.join_strings([""]) == ""
    assert StringUtils.join_strings(["Hello", "", "world"]) == "Hello  world"
    assert StringUtils.join_strings([]) == ""


def test_join_strings_negative():
    # negative
    assert StringUtils.join_strings(None) is None


def test_is_palindrome_positive():
    # positive
    assert StringUtils.is_palindrome("А роза упала на лапу Азора") is True
    assert StringUtils.is_palindrome("madam") is True


def test_is_palindrome_negative():
    # negative
    assert StringUtils.is_palindrome("Тест") is False
    assert StringUtils.is_palindrome(None) is False
    assert StringUtils.is_palindrome("") is True
