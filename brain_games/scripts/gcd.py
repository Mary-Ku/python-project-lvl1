"""Модуль содержит игру 'Greatest Common Divisor'."""


import prompt  # type: ignore[import-untyped]

from brain_games.cli import get_two_any_numbers, logger, welcome_user


def get_gcd(number_1: int, number_2: int) -> int:
    """Возвращает НОД чисел number_1 и number_2.

    Returns:
        int: наибольший общий делитель двух чисел.

    """
    if number_2 == 0:
        return number_1

    new_number_1 = number_2
    new_number_2 = number_1 % number_2

    return get_gcd(new_number_1, new_number_2)


def main() -> None:
    """Точка входа игры 'Greatest Common Divisor'."""
    name = welcome_user()
    if not name:
        return

    logger.info('Find the greatest common divisor of given numbers.')

    for _try in range(3):
        number_1, number_2 = get_two_any_numbers(1, 100)
        correct_answer = get_gcd(number_1, number_2)

        answer = prompt.string(f'Question: {number_1} {number_2} ')
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
