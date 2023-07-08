from exceptions import InvalidInputException, InvalidRowsException, InvalidLevelException
from typing import Callable


def unordered_list() -> str:
    rows = get_rows()
    elements = ''

    for row in range(1, rows + 1):
        cmd = input('Row #{}: '.format(row))
        elements += ('* {}\n'.format(cmd))

    return elements


def ordered_list() -> str:
    rows = get_rows()
    elements = ''

    for row in range(1, rows + 1):
        cmd = input('Row #{}: '.format(row))
        elements += ('{}. {}\n'.format(row, cmd))

    return elements


def plain() -> str:
    return input('Text: ')


def bold() -> str:
    text = input('Text: ')
    return '**{}**'.format(text)


def italic() -> str:
    text = input('Text: ')
    return '*{}*'.format(text)


def header() -> str:
    level = get_level()
    text = input('Text: ')
    return '{} {}\n'.format('#' * level, text)


def inline_code() -> str:
    text = input('Text: ')
    return '`{}`'.format(text)


def link() -> str:
    label = input('Label: ')
    url = input('URL: ')
    return '[{}]({})'.format(label, url)


def new_line() -> str:
    return '\n'


def validate_rows(rows: int) -> None:
    """Raise InvalidRowsException if rows < 1"""
    if rows < 1:
        raise InvalidRowsException("The number of rows should be greater than zero")


def validate_level(level: int) -> None:
    """Raise InvalidLevelException if level <1 or >6"""
    if level < 1 or level > 6:
        raise InvalidLevelException("The level should be within the range of 1 to 6")


def get_validated_input(prompt: str, validation_func: Callable[[str], int]) -> int:
    """Get input and validate with callable validation function"""
    while True:
        user_input = input(prompt)
        try:
            value = validation_func(user_input)
            return value
        except InvalidInputException as e:
            print(e)


def get_rows() -> int:
    """Get input for rows"""
    def validate_rows_input(input_str: str) -> int:
        try:
            rows = int(input_str)
            validate_rows(rows)
            return rows
        except ValueError:
            raise InvalidInputException("This is not a number")
        except InvalidRowsException as e:
            raise InvalidInputException(e)

    prompt = "Number of rows: "
    return get_validated_input(prompt, validate_rows_input)


def get_level() -> int:
    """Get input for level"""
    def validate_level_input(input_str: str) -> int:
        try:
            level = int(input_str)
            validate_level(level)
            return level
        except ValueError:
            raise InvalidInputException("This is not a number")
        except InvalidLevelException as e:
            raise InvalidInputException(e)

    prompt = "Level: "
    return get_validated_input(prompt, validate_level_input)
