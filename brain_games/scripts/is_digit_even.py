"""Модуль содержит функционал для игры 'Is Digit Even?'."""

from secrets import choice


def get_main_data() -> tuple[str, str]:
    """Подготавливает условие задачи и ответ для игры.

    Returns:
        tuple[str, str]:
            str: случайное число для вопроса игроку.
            str: правильный ответ о чётности числа.

    """
    number = choice(range(1, 1000))
    correct_answer = 'yes' if number % 2 == 0 else 'no'

    return str(number), correct_answer
