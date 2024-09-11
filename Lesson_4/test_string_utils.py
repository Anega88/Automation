import pytest
from String_Utils import StringUtils

StrUtils = StringUtils()


# ПОЗИТИВНЫЕ ПРОВЕРКИ
# Большая первая буква
@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [
    ("буква", "Буква"),  # с маленькой буквы
    ("май месяц", "Май месяц"),  # текст с пробелом
    ("январь 23", "Январь 23"),  # буквы и цифры
    ("я", "Я"),  # одна буква
    ("big", "Big")  # латиница
    ])
def test_big_first_letter(string, result):
    strUtils = StringUtils()
    res = strUtils.capitilize(string)
    assert res == result


# Удаление пробелов в начале
@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [
    (" Пробел", "Пробел"),  # слово
    ("   ", "  "),  # несколько пробелов
    (" Удалить пробел", "Удалить пробел"),  # слова с пробелом в середине
    (" 12345", "12345"),  # цифры
    (" 12 345", "12 345")  # цифры с пробелом в середине
    ])
def test_delete_space(string, result):
    strUtils = StringUtils()
    res = strUtils.trim(string)
    assert res == result


# Из строки в список с разделителем
@pytest.mark.positive_test
def test_string_to_list_with_separator():
    strUtils = StringUtils()
    res = strUtils.to_list("один-два-три-четыре-пять", "-")  # через дефис
    assert res == ["один", "два", "три", "четыре", "пять"]


@pytest.mark.positive_test
def test_string_to_list_without_separator_words():
    strUtils = StringUtils()
    res = strUtils.to_list("один,два,три,"
                           "четыре,пять")
    # не указывая разделитель
    assert res == ["один", "два", "три", "четыре", "пять"]


@pytest.mark.positive_test
def test_string_to_list_without_separator_nums():
    strUtils = StringUtils()
    res = strUtils.to_list("1,2,3,4,5")
    # цифры через запятую, не указывая разделитель
    assert res == ["1", "2", "3", "4", "5"]


@pytest.mark.positive_test
def test_string_to_list_dash():
    strUtils = StringUtils()
    res = strUtils.to_list("1-2-3-4-5", "-")  # цифры через дефис
    assert res == ["1", "2", "3", "4", "5"]


@pytest.mark.positive_test
def test_string_to_list_colon():
    strUtils = StringUtils()
    res = strUtils.to_list("один:два:три:четыре:пять", ":")  # через двоеточие
    assert res == ["один", "два", "три", "четыре", "пять"]


@pytest.mark.positive_test
def test_string_to_list_space():
    strUtils = StringUtils()
    res = strUtils.to_list("один два три четыре пять", " ")  # через пробелы
    assert res == ["один", "два", "три", "четыре", "пять"]


# Поиск символа
@pytest.mark.positive_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("Найти символ", "л", True),  # в нижнем регистре - True
    ("Найти символ", "Н", True),  # в верхнем регистре - True
    ("Найти символ", " ", True)   # найти проблел, как символ.
])
def test_look_for_letter_true(string, symbol, result):
    strUtils = StringUtils()
    res = strUtils.contains(string, symbol)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("Найти символ", "п", False),  # в нижнем регистре - False
    ("Найти символ", "К", False),  # в верхнем регистре - False
    ("Найти символ", ".", False)  # найти точку "."
])
def test_look_for_letter_false(string, symbol, result):
    strUtils = StringUtils()
    res = strUtils.contains(string, symbol)
    assert res == result


# Удаление указанных символов
@pytest.mark.positive_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("Найти символ и удалить", "а", "Нйти символ и удлить"),
    # символ в нижнем регистре
    ("Найти символ и удалить", "Н", "айти символ и удалить"),
    # символ в верхнем регистре
    ("Найти символ и удалить", " символ", "Найти и удалить"),
    # целое слово
    ("Найти номер 123", "123", "Найти номер "),
    # цифры
    ("8 900 356 78 98", " ", "89003567898"),
    # пробел
    ("8-900-356-78-98", "-", "89003567898")
    # дефис
])
def test_find_and_delete_letter(string, symbol, result):
    strUtils = StringUtils()
    res = strUtils.delete_symbol(string, symbol)
    assert res == (result)


# Соответствие первого символа
@pytest.mark.positive_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("Первая буква", "П", True),
    # в верхнем регистре - True
    ("первая буква", "п", True),
    # в нижнем регистре - True
    ("First letter", "F", True),
    # латиница в верхнем регистре - True
    ("first letter", "f", True),
    # латиница в нижнем регистре - True
    ("1257896", "1", True)  # цифра - True
 ])
def test_compare_first_letter_true(string, symbol, result):
    strUtils = StringUtils()
    res = strUtils.starts_with(string, symbol)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("первая буква", "б", False),
    # в нижнем регистре - False
    ("Первая буква", "Б", False),
    # в верхнем регистре - False
    ("First letter", "n", False),
    # латиница в верхнем регистре - False
    ("first letter", "N", False),
    # латиница в нижнем регистре - False
    ("первая буква", "П", False),
    # в верхнем регистре, когда первый символ текста в нижнем - False
    ("Первая буква", "п", False),
    # в нижнем регистре, когда первый символ текста в верхнем - False
    ("1257896", "2", False)
    # цифра - False
])
def test_compare_first_letter_false(string, symbol, result):
    strUtils = StringUtils()
    res = strUtils.starts_with(string, symbol)
    assert res == result


# Соответствие последнего символа
@pytest.mark.positive_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("Последняя буква", "а", True),
    # в нижнем регистре - True
    ("Последняя буквА", "А", True),
    # в верхнем регистре - True
    ("1257896", "6", True),
    # цифра - True
    ("Проверка!", "!", True),
    # знак препинания "!" - True
    ("Проверка ", " ", True),
    # пробел - True
    ("Last letteR", "R", True),
    # латиница в верхнем регистре - True
    ("Last letter", "r", True)
    # латиница в нижнем регистре - True
 ])
def test_compare_end_letter_true(string, symbol, result):
    strUtils = StringUtils()
    res = strUtils.end_with(string, symbol)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("Последняя буква", "о", False),
    # в нижнем регистре - False
    ("Последняя буквА", "Т", False),
    # в верхнем регистре - False
    ("1257896", "8", False),
    # цифра - False
    ("Проверка.", "!", False),
    # знак препинания "!" - False
    ("Проверка!", " ", False),
    # пробел - False
    ("Last letteR", "K", False),
    # латиница в верхнем регистре - False
    ("Last letter", "y", False),
    # латиница в нижнем регистре - False
    ("Last letter", "R", False),
    # в верхнем регистре, когда послений символ текста в нижнем - False
    ("Last letteR", "r", False)
    # в нижнем регистре, когда послений символ текста в верхнем - False
 ])
def test_compare_end_letter_false(string, symbol, result):
    strUtils = StringUtils()
    res = strUtils.end_with(string, symbol)
    assert res == result


# Пустая строка или нет
@pytest.mark.positive_test
@pytest.mark.parametrize(('string', 'result'), [
    ("", True),
    # пустое поле - True
    (" ", True)
    # пробел - True
])
def test_string_empty_true(string, result):
    strUtils = StringUtils()
    res = strUtils.is_empty(string)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize(('string', 'result'), [
    ("Не пустая", False),
    # строка не пустая - False
    ("...", False),
    # троеточие - False
    ("123", False)
    # цифры - False
 ])
def test_string_empty_false(string, result):
    strUtils = StringUtils()
    res = strUtils.is_empty(string)
    assert res == result


# Из списка в строку с разделителем
@pytest.mark.positive_test
def test_list_to_string_dash():
    strUtils = StringUtils()
    result = strUtils.list_to_string(
        ["один", "два", "три", "четыре", "пять"], "-"
        )
    # через дефис
    assert result == ("один-два-три-четыре-пять")


@pytest.mark.positive_test
def test_list_to_string_default():
    strUtils = StringUtils()
    result = strUtils.list_to_string(["один", "два", "три", "четыре", "пять"])
    # по умолчанию ","
    assert result == ("один, два, три, четыре, пять")


@pytest.mark.positive_test
def test_list_to_string_space_nums():
    strUtils = StringUtils()
    result = strUtils.list_to_string(["1", "2", "3", "4", "5"], " ")
    # пробел цифры
    assert result == ("1 2 3 4 5")


@pytest.mark.positive_test
def test_list_to_string_space_words():
    strUtils = StringUtils()
    result = strUtils.list_to_string(
        ["один", "два", "три", "четыре", "пять"], " "
        )
    # пробел слова
    assert result == ("один два три четыре пять")


@pytest.mark.positive_test
def test_list_to_string_plus():
    strUtils = StringUtils()
    result = strUtils.list_to_string(["1", "2", "3", "4", "5"], "+")
    # знак сложения
    assert result == ("1+2+3+4+5")


@pytest.mark.positive_test
def test_list_to_string_letter():
    strUtils = StringUtils()
    result = strUtils.list_to_string(["1", "2", "3", "4", "5"], "о")
    # буква, как разделитель среди цифр
    assert result == ("1о2о3о4о5")


# НЕГАТИВНЫЕ ПРОВЕРКИ
# Большая первая буква
@pytest.mark.negative_test
@pytest.mark.parametrize('string, result', [
    ("", ""),
    # пустая строка
    (" буква", " буква"),
    # первый символ - пробел
    ("!буква", "!буква"),
    # первый символ - знак препинания
    (None, None)
    # проверка на None
  ])
def test_big_first_letter_negative(string, result):
    strUtils = StringUtils()
    if string is None:
        with pytest.raises(TypeError):
            strUtils.capitilize(string)
    else:
        res = strUtils.capitilize(string)
        assert res == result


# Удаление пробелов в начале
@pytest.mark.negative_test
@pytest.mark.parametrize('string, result', [
    ("", ""),
    # пустая строка
    (" ", ""),
    # только пробел
    (None, None)
    # проверка на None
    ])
def test_delete_space_negative(string, result):
    strUtils = StringUtils()
    if string is None:
        with pytest.raises(TypeError):
            strUtils.trim(string)
    else:
        res = strUtils.trim(string)
        assert res == result


# Из строки в список с разделителем
@pytest.mark.negative_test
def test_string_to_list_with_separator_negative():
    strUtils = StringUtils()
    res = strUtils.to_list("", "-")
    # пустая строка, разделитель есть
    assert res == []


@pytest.mark.negative_test
def test_string_to_list_no_separator_string():
    strUtils = StringUtils()
    res = strUtils.to_list("", "")
    # пустая строка, пустой разделитель
    assert res == []


@pytest.mark.negative_test
def test_string_to_list_with_none():
    strUtils = StringUtils()
    res = strUtils.to_list(None, None)
    # проверка на None
    assert res is None


# Поиск символа
@pytest.mark.negative_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("", "л", False),
    # пустая строка
    ("Слово", "", True),
    # не указан искомый символ
    ("Слово", "Сло", True),
    # несколько символов
    (None, None, None)
    # проверка на None
])
def test_look_for_letter(string, symbol, result):
    strUtils = StringUtils()
    if string is None or symbol is None:
        with pytest.raises(TypeError):
            strUtils.contains(string, symbol)
    else:
        res = strUtils.contains(string, symbol)
        assert res == result


# Удаление указанных символов
@pytest.mark.negative_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("", "а", ""),
    # пустая строка, искомый символ есть
    ("Удали меня", "", "Удали меня"),
    # строка есть, искомый символ пуст
    ("Удали меня", "Удали меня", ""),
    # строка == искомым символам
    (None, None, None)
    # проверка на None
])
def test_find_and_delete_letter_negative(string, symbol, result):
    strUtils = StringUtils()
    if string is None or symbol is None:
        with pytest.raises(TypeError):
            strUtils.delete_symbol(string, symbol)
    else:
        res = strUtils.delete_symbol(string, symbol)
        assert res == result


# Соответствие первого символа
@pytest.mark.negative_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("", "П", False),
    # пустая строка, есть искомый символ
    ("", "", True),
    # пустая строка, пустой искомый символ
    ("Найди меня", "", True),
    # пустой искомый символ
    ("Найди меня", "На", True),
    # несколько искомых символов
    (None, None, None)
    # проверка на None
   ])
def test_compare_first_letter(string, symbol, result):
    strUtils = StringUtils()
    if string is None or symbol is None:
        with pytest.raises(TypeError):
            strUtils.starts_with(string, symbol)
    else:
        res = strUtils.starts_with(string, symbol)
        assert res == result


# Соответствие последнего символа
@pytest.mark.negative_test
@pytest.mark.parametrize(('string', 'symbol', 'result'), [
    ("", "а", False),
    # пустая строка, есть искомый символ
    ("", "", True),
    # пустая строка, пустой искомый символ
    ("Символ", "", True),
    # пустой искомый символ
    ("Символ", "ол", True),
    # несколько искомых символов
    (None, None, None)
    # проверка на None
    ])
def test_compare_end_letter(string, symbol, result):
    strUtils = StringUtils()
    if string is None or symbol is None:
        with pytest.raises(TypeError):
            strUtils.end_with(string, symbol)
    else:
        res = strUtils.end_with(string, symbol)
        assert res == result


# Из списка в строку с разделителем
@pytest.mark.negative_test
def test_list_to_string_empty_list():
    strUtils = StringUtils()
    result = strUtils.list_to_string([], "-")
    # пустой список
    assert result == ("")


@pytest.mark.negative_test
def test_list_to_string_few_separators():
    strUtils = StringUtils()
    result = strUtils.list_to_string(["один", "два", "три",
                                      "четыре", "пять"], "--")
    # разделитель несколько символов
    assert result == ("один--два--три--четыре--пять")


@pytest.mark.negative_test
def test_list_to_string_no_separators():
    strUtils = StringUtils()
    result = strUtils.list_to_string(["один", "два", "три",
                                      "четыре", "пять"], "")
    # разделитель пуст
    assert result == ("одиндватричетырепять")


@pytest.mark.negative_test
def test_list_to_string_none():
    strUtils = StringUtils()
    result = strUtils.list_to_string(None, None)
    # проверка на None
    assert result is None
