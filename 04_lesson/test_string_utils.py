import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, expected', [
    ('привет, друг', 'Привет, друг'),
    ('hello world', 'Hello world'),
    ('Стало холодно', 'Стало холодно')])
def test_capitalize_positive(input_text, expected):
    assert string_utils.capitalize(input_text) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, expected', [
    ('', ''),
    ('   ', '   '),
    ('1234ok', '1234ok'),
    ('!здравствуй', '!здравствуй'),
    ('   привет', '   привет'), ])
def test_capitalize_negative(input_text, expected):
    assert string_utils.capitalize(input_text) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text', [(123), (True), (False), (["привет"])])
def test_capitalize_negative_attribute_error(input_text):
    with pytest.raises(AttributeError):
        string_utils.capitalize(input_text)


@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, expected', [
    (" кошка", "кошка"),
    ("   хлопушка", "хлопушка"),
    ("стол", "стол"),
    (" кому на Руси жить хорошо", "кому на Руси жить хорошо"),
    ("зайка  ", "зайка  "),
    ("! Важно", "! Важно")])
def test_trim_positive(input_text, expected):
    assert string_utils.trim(input_text) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, expected', [
    (" ", ""),
    ("      ", ""),
    ("", ""), ])
def test_trim_negative(input_text, expected):
    assert string_utils.trim(input_text) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, symbol, expected', [
    ('кот', 'т', True),
    ('корова', 'о', True),
    ('знаки зодиака', 'щ', False),
    ('Hello', 'l', True),
    ('London', 'n', True),
    ('Вася', 'в', False),
    ('Rhjn', 'R', True)])
def test_contains_positive(input_text, symbol, expected):
    assert string_utils.contains(input_text, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, symbol, expected', [
    ("", "", True),
    ("   ", "   ", True)])
def test_contains_negative(input_text, symbol, expected):
    assert string_utils.contains(input_text, symbol) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, symbol, expected', [
    ('кот', 'т', "ко"),
    ('корова', 'о', 'крва'),
    ('знаки зодиака', 'щ', "знаки зодиака"),
    ('Hello', 'l', 'Heo'),
    ('London', 'n', 'Lodo'),
    ('Вася', 'в', 'Вася'),
    ('Rhjn', 'R', 'hjn'),
    ('    всё будет хорошо  ', ' ', 'всёбудетхорошо'),
    ('все ели ёлки', 'ё', 'все ели лки'),
    ('все ели ёлки', 'е', 'вс ли ёлки')])
def test_delete_symbol_positive(input_text, symbol, expected):
    assert string_utils.delete_symbol(input_text, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, symbol, expected', [
    ("", "", ""),
    ("", " ", ""),
    ("re-re-re", "", "re-re-re"),
])
def test_delete_symbol_negative(input_text, symbol, expected):
    assert string_utils.delete_symbol(input_text, symbol) == expected
