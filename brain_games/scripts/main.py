"""Модуль содержит точку входа проекта Brain Games."""

from brain_games.cli import logger, welcome_user


def main() -> None:
    """Точка входа проекта Brain Games."""
    logger.info('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
