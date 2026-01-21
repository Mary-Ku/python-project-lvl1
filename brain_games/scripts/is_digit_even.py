from secrets import randbelow

import prompt

from brain_games.cli import welcome_user

_WRONG_ANSWERS_MAP = {
    'yes': 'no',
    'no': 'yes',
}


def is_answer_correct(number, answer):
    # Игра сравнивает чётность числа с ответом игрока
    # Проверка чётности числа
    is_even = number % 2 == 0

    # Подбираем предполагаемый правильный ответ
    excepted_answer = 'yes' if is_even else 'no'

    # Сравниваем предполагаемый ответ с фактическим
    return answer.lower() == excepted_answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    if not name:
        return

    print('Answer "yes" if the number is even, otherwise answer "no".')

    # Игрок считается победителем, если даст 3 правильных ответа
    for _try in range(3):
        # Игра выбирает случайное число от 1 до 100
        number = randbelow(101)

        # Игра предлагает число, пользователь вводит ответ
        answer = prompt.string(f'Question: {number}')
        print(f'Your answer: {answer}')

        formatted_answer = answer.lower().strip()

        # Если ответ правильный - игра продолжается
        if is_answer_correct(number, formatted_answer):
            print('Correct!')
        else:
            correct_answer = _WRONG_ANSWERS_MAP[formatted_answer]

            print(f'"{formatted_answer}" is wrong answer ;(. Correct answer is "{correct_answer}"')
            print(f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
