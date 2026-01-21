import logging

from brain_games.cli import welcome_user

logger = logging.getLogger(__name__)


def main() -> None:
    logger.info('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
