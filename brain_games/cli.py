"""Модуль содержит базовые функции."""

import logging

import prompt  # type: ignore[import-untyped]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO,
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
        logger.info("It's impossible to continue without your name. Maybe next time.")
        return None

    logger.info('Hello, %s!', name)
    return name
