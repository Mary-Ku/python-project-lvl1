"""Модуль содержит точку входа в игру 'Arithmetic Progression'."""

from brain_games.cli import run_game
from brain_games.scripts.arithmetic_progression import get_main_data
from brain_games.types import GetMainDataFunc


@run_game
def run_arithmetic_progression() -> tuple[str, GetMainDataFunc]:
    """Запускает игру 'Arithmetic Progression'.

    Returns:
        tuple[str, Func]
            str: Приветственное сообщение игры.
            Func: Функция, возвращающая условие задачи и правильный ответ.

    """
    welcome_message = 'What number is missing in the progression?'
    return welcome_message, get_main_data


def main() -> None:
    """Точка входа игры 'Arithmetic Progression'."""
    run_arithmetic_progression()


if __name__ == '__main__':
    main()
