"""Модуль содержит игру 'Arithmetic Progression'."""

from secrets import choice


def get_main_data() -> tuple[str, str]:
    """Подготавливает условие задачи и ответ для игры.

    Returns:
        tuple[str, str]:
            str: прогрессия с одним пропущенным числом.
            str: пропущенное число.

    """
    some_range = range(1, 100)
    start_number, step = choice(some_range), choice(some_range)

    progression: list[int] = [
        start_number + step * index for index in range(10)
    ]

    formatted_progression: list[str] = list(map(str, progression))
    random_number = choice(formatted_progression)

    condition = ' '.join(formatted_progression).replace(random_number, '..')

    return condition, random_number
