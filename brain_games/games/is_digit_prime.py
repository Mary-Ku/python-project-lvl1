"""Модуль содержит точку входа в игру 'Is Digit Prime?'."""

from brain_games.cli import run_game
from brain_games.scripts.is_digit_prime import get_main_data
from brain_games.types import GetMainDataFunc


@run_game
def run_is_digit_prime() -> tuple[str, GetMainDataFunc]:
    """Запускает игру 'Is Digit Prime?'.

    Returns:
        tuple[str, Func]
            str: Приветственное сообщение игры.
            Func: Функция, возвращающая условие задачи и правильный ответ.

    """
    welcome_message = (
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )

    return welcome_message, get_main_data


def main() -> None:
    """Точка входа игры 'Is Digit Prime?'."""
    run_is_digit_prime()


if __name__ == '__main__':
    main()
