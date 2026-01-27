"""Модуль содержит точку входа в игру 'Calculator'."""

import prompt  # type: ignore[import-untyped]

from brain_games.cli import logger, welcome_user
from brain_games.scripts.calculator import get_main_data


def main() -> None:
    """Точка входа игры 'Calculator'."""
    name = welcome_user()
    if not name:
        return

    logger.info('What is the result of the expression?')

    for _try in range(3):
        condition, correct_answer = get_main_data()

        answer = prompt.string(f'Question: {condition} ')
        logger.info('Your answer: %s', answer)

        if correct_answer == int(answer):
            logger.info('Correct!')
        else:
            logger.info(
                "'%s' is wrong answer ;(. Correct answer is '%s'"
                "\n Let's try again, %s!",
                answer, correct_answer, name,
            )
            return

    logger.info('Congratulations, %s!', name)


if __name__ == '__main__':
    main()
