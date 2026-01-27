"""Модуль содержит базовые функции."""

import logging
from secrets import choice

import prompt  # type: ignore[import-untyped]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def welcome_user() -> str | None:
    """Спрашивает имя пользователя.

    Returns:
        str or None
            str, если введено имя
            None, если вместо имени введён пробел

    """
    logger.info('Welcome to the Brain Games!')
    name: str | None = prompt.string('May I have your name? ').strip()
    if not name:
        logger.info(
            "It's impossible to continue without your name. Maybe next time.",
        )
        return None

    logger.info('Hello, %s!', name)
    return name


def get_two_any_numbers(
    first_in_range: int,
    last_in_range: int,
) -> tuple[int, int]:
    """Возвращает два случайных числа из переданного диапазона.

    Args:
        first_in_range (int): начало диапазона.
        last_in_range (int): конец диапазона.

    Returns:
        tuple[int, int]: два случайных числа из переданного диапазона.

    """
    any_range = range(first_in_range, last_in_range)
    return choice(any_range), choice(any_range)
