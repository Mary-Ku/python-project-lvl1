"""Модуль содержит игру 'Greatest Common Divisor'."""

from secrets import choice


def get_main_data() -> tuple[str, str]:
    """Подготавливает условие задачи и ответ для игры.

    Returns:
        tuple[str, str]:
            str: условие задачи для вопроса игроку.
            str: правильный ответ на вопрос.

    """
    some_range = range(1, 100)
    number_1, number_2 = choice(some_range), choice(some_range)

    condition = f'{number_1} {number_2}'
    correct_answer = get_gcd(number_1, number_2)

    return condition, str(correct_answer)


def get_gcd(number_1: int, number_2: int) -> int:
    """Рекурсия вычисления НОД'а двух чисел.

    Returns:
        int: наибольший общий делитель двух чисел.

    """
    if number_2 == 0:
        return number_1

    new_number_1 = number_2
    new_number_2 = number_1 % number_2

    return get_gcd(new_number_1, new_number_2)
