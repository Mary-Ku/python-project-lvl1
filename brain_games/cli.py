import prompt


def welcome_user():
    name = prompt.string('May I have your name? ').strip()
    if not name:
        print('It\'s impossible to continue without your name. Maybe next time.')
        return
    else:
        print(f'Hello, {name}!')
        return name
