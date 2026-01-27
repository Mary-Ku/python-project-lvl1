"""Модуль содержит игру 'Is Digit Prime?'."""

from secrets import choice

import prompt  # type: ignore[import-untyped]

from brain_games.cli import YES_NO_WRONG_ANSWERS_MAP, logger, welcome_user


def is_digit_prime(number: int) -> bool:
    """Проверяет, простое ли число, и сравнивает результат с ответом игрока.

    Args:
        number (int): Число, которое проверяется.

    Returns:
        bool: True, если число простое, иначе False.

    """
    dividers = [2, 3, 5]

    if number in dividers:
        return True

    # Если хоть одно число делится на предложенный делитель - оно не простое
    for divider in dividers:
        if number % divider == 0:
            return False

    return True


def main() -> None:
    """Точка входа игры 'Is Digit Prime?'."""
    name = welcome_user()
    if not name:
        return

    logger.info('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _try in range(3):
        number = choice(range(2, 1000))
        correct_answer = 'yes' if is_digit_prime(number) else 'no'

        answer = prompt.string(f'Question: {number}')
        logger.info('Your answer: %s', answer)

        formatted_answer = answer.lower().strip()

        # Если ответ правильный - игра продолжается
        if formatted_answer == correct_answer:
            logger.info('Correct!')
        else:
            correct_answer = YES_NO_WRONG_ANSWERS_MAP[formatted_answer]

            logger.info(
                '"%s" is wrong answer ;(. Correct answer is "%s"'
                "\n Let's try again, %s!",
                formatted_answer, correct_answer, name,
            )
            return

    logger.info('Congratulations, %s!', name)


if __name__ == '__main__':
    main()
