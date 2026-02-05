"""Модуль содержит точку входа в игру 'Greatest Common Divisor'."""

from brain_games.cli import run_game
from brain_games.scripts.gcd import get_main_data
from brain_games.types import GetMainDataFunc


@run_game
def run_gcd() -> tuple[str, GetMainDataFunc]:
    """Запускает игру 'Greatest Common Divisor'.

    Returns:
        tuple[str, Func]
            str: Приветственное сообщение игры.
            Func: Функция, возвращающая условие задачи и правильный ответ.

    """
    welcome_message = 'Find the greatest common divisor of given numbers.'
    return welcome_message, get_main_data


def main() -> None:
    """Точка входа игры 'Greatest Common Divisor'."""
    run_gcd()


if __name__ == '__main__':
    main()
