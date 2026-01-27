"""Модуль содержит игру 'Arithmetic Progression'."""

from secrets import choice

import prompt  # type: ignore[import-untyped]

from brain_games.cli import get_two_any_numbers, logger, welcome_user


def get_progression(start_number: int, step: int) -> tuple[str, int]:
    """Возвращает прогрессию с одним пропущенным числом.

    Args:
        start_number: int, первое число прогрессии
        step: int, шаг прогрессии

    Returns:
        tuple: прогрессия с пропущенным числом и пропущенное число.

    """
    progression: list[int] = [
        start_number + step * index for index in range(10)
    ]

    formatted_progression: list[str] = list(map(str, progression))
    random_number = choice(formatted_progression)

    condition = ' '.join(formatted_progression).replace(random_number, '..')

    return condition, int(random_number)


def main() -> None:
    """Точка входа игры 'Arithmetic Progression'."""
    name = welcome_user()
    if not name:
        return

    logger.info('What number is missing in the progression?')

    # Игрок считается победителем, если даст 3 правильных ответа
    for _try in range(3):
        start_number, step = get_two_any_numbers(1, 100)
        condition, correct_answer = get_progression(start_number, step)

        # Игрок вводит ответ
        answer = prompt.string(f'Question: {condition} ')
        logger.info('Your answer: %s', answer)

        # Если ответ правильный - игра продолжается
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
