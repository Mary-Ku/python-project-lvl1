"""Модуль содержит точку входа проекта Brain Games."""

from brain_games.cli import welcome_user


def main() -> None:
    """Точка входа проекта Brain Games."""
    welcome_user()


if __name__ == '__main__':
    main()
