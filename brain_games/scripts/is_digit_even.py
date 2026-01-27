"""Модуль содержит игру 'Is Digit Even?'."""

from secrets import randbelow

import prompt  # type: ignore[import-untyped]

from brain_games.cli import YES_NO_WRONG_ANSWERS_MAP, logger, welcome_user


def is_answer_correct(number: int, answer: str) -> bool:
    """Проверяет, совпадает ли ответ игрока с чётностью числа.

    Args:
        number (int): Число, чётность которого проверяется.
        answer (str): Ответ игрока ('yes' или 'no').

    Returns:
        bool: True, если ответ игрока равен ожидаемому, иначе False.

    """
    is_even = number % 2 == 0

    excepted_answer = 'yes' if is_even else 'no'
    return answer.lower() == excepted_answer


def main() -> None:
    """Точка входа игры 'Is Digit Even?'."""
    name = welcome_user()
    if not name:
        return

    logger.info('Answer "yes" if the number is even, otherwise answer "no".')

    # Игрок считается победителем, если даст 3 правильных ответа
    for _try in range(3):
        # Игра выбирает случайное число от 1 до 100
        number = randbelow(101)

        # Игра предлагает число, пользователь вводит ответ
        answer = prompt.string(f'Question: {number}')
        logger.info('Your answer: %s', answer)

        formatted_answer = answer.lower().strip()

        # Если ответ правильный - игра продолжается
        if is_answer_correct(number, formatted_answer):
            logger.info('Correct!')
        else:
            correct_answer = YES_NO_WRONG_ANSWERS_MAP[formatted_answer]

            logger.info(
                '"%s" is wrong answer ;(. Correct answer is "%s"',
                formatted_answer,
                correct_answer,
            )
            logger.info("Let's try again, %s!", name)
            return

    logger.info('Congratulations, %s!', name)


if __name__ == '__main__':
    main()
