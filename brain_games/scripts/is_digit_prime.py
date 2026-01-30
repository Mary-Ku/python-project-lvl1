"""Модуль содержит функционал для игры  'Is Digit Prime?'."""

from secrets import choice


def is_digit_prime(number: int) -> bool:
    """Проверяет, является ли переданное число простым.

    Простое число — натуральное число больше 1, имеющее ровно два
    различных натуральных делителя: 1 и само себя.

    Args:
        number: Целое число для проверки.

    Returns:
        True, если число простое; False в противном случае.

    """
    if number <= 1:
        return False

    if number <= 3:  # noqa: PLR2004
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    candidate_divisor = 5
    while candidate_divisor * candidate_divisor <= number:
        if (
            number % candidate_divisor == 0
            or number % (candidate_divisor + 2) == 0
        ):
            return False

        candidate_divisor += 6

    # Если ни один делитель не подошёл — число простое
    return True


def get_main_data() -> tuple[int, str]:
    """Подготавливает условие задачи и ответ для игры.

    Returns:
        tuple[str, str]:
            str: случайное число для вопроса игроку.
            str: правильный ответ о чётности числа.

    """
    number = choice(range(2, 1000))
    correct_answer = 'yes' if is_digit_prime(number) else 'no'

    return number, correct_answer
