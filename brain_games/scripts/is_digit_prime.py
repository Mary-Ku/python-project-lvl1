"""Модуль содержит игру 'Is Digit Prime?'."""

from secrets import choice

import prompt  # type: ignore[import-untyped]

from brain_games.cli import YES_NO_WRONG_ANSWERS_MAP, logger, welcome_user


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
