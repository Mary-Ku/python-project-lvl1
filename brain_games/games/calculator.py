"""Модуль содержит точку входа в игру 'Calculator'."""

from brain_games.cli import run_game
from brain_games.scripts.calculator import get_main_data
from brain_games.types import GetMainDataFunc


@run_game
def run_calculator() -> tuple[str, GetMainDataFunc]:
    """Запускает игру 'Calculator'.

    Returns:
        tuple[str, Func]
            str: Приветственное сообщение игры.
            Func: Функция, возвращающая условие задачи и правильный ответ.

    """
    welcome_message = 'What is the result of the expression?'

    return welcome_message, get_main_data


def main() -> None:
    """Точка входа игры 'Calculator'."""
    run_calculator()


if __name__ == '__main__':
    main()
