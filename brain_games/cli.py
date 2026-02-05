"""Модуль содержит базовые функции."""

import logging
from collections.abc import Callable

import prompt  # type: ignore[import-untyped]

from brain_games.types import RunGameFunc

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def run_game(func: RunGameFunc) -> Callable[..., None]:
    """Декоратор, оборачивающий функцию игры и запускающий игровой процесс.

    Args:
        func: Функция, возвращающая приветственное сообщение и функцию игры.

    Returns:
        Callable[..., None]: Обёрнутая функция,
        запускает игру с логикой 3-х попыток.

    """
    def wrapper() -> None:
        name = welcome_user()
        if not name:
            return

        welcome_message, game_main_function = func()
        logger.info(welcome_message)

        for _try in range(3):
            condition, correct_answer = game_main_function()

            answer = prompt.string(f'Question: {condition} ')
            logger.info('Your answer: %s', answer)

            if correct_answer == answer.strip().lower():
                logger.info('Correct!')
            else:
                logger.info(
                    "'%s' is wrong answer ;(. Correct answer is '%s'"
                    "\n Let's try again, %s!",
                    answer, correct_answer, name,
                )
                return

        logger.info('Congratulations, %s!', name)
        return

    return wrapper


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
