"""Модуль содержит игру 'Calculator?'."""

import operator
from secrets import choice

import prompt  # type: ignore[import-untyped]

from brain_games.cli import get_two_any_numbers, logger, welcome_user


def main() -> None:
    """Точка входа игры 'Calculator'."""
    name = welcome_user()
    if not name:
        return

    logger.info('What is the result of the expression?')

    for _try in range(3):
        number_1, number_2 = get_two_any_numbers(1, 50)

        # Выбираем случайный оператор
        any_operator = choice(['+', '-', '*'])

        # Словарь для сопоставления символа операции с функцией
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }

        math_function = operators[any_operator]
        correct_answer = math_function(number_1, number_2)

        expression = f'{number_1} {any_operator} {number_2}'

        answer = prompt.string(f'Question: {expression} ')
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
