"""Модуль содержит функционал для игры 'Calculator'."""

import operator
from secrets import choice

from brain_games.cli import get_two_any_numbers


def get_main_data() -> tuple[str, str]:
    """Подготавливает условие задачи и ответ для игры.

    Returns:
        tuple[str, str]:
            str: условие задачи для вопроса игроку.
            str: правильный ответ на вопрос.

    """
    number_1, number_2 = get_two_any_numbers(1, 50)
    any_operator = choice(['+', '-', '*'])

    # Словарь для сопоставления символа операции с функцией
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    math_function = operators[any_operator]
    correct_answer = math_function(number_1, number_2)

    condition = f'{number_1} {any_operator} {number_2}'
    return condition, correct_answer
