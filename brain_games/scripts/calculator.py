"""Модуль содержит функционал для игры 'Calculator'."""

import operator
from secrets import choice


def get_main_data() -> tuple[str, str]:
    """Подготавливает условие задачи и ответ для игры.

    Returns:
        tuple[str, str]:
            str: условие задачи для вопроса игроку.
            str: правильный ответ на вопрос.

    """
    some_range = range(1, 50)
    number_1, number_2 = choice(some_range), choice(some_range)
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
    return condition, str(correct_answer)
