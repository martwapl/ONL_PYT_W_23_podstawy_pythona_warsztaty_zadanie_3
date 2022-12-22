def user_input():
    """
    Return proper value provided by user
    :rtype str
    :return:value provided by user from ['za mało', 'za dużo', 'wygrałeś]
    """
    possible_input = ['za mało', 'za dużo', 'wygrałeś']
    while True:
        user_answer = input('Drogi graczu, zgadłem? ').lower()
        if user_answer not in possible_input:
            print(f'Możliwe odpowiedzi to: {possible_input}. Wprowadź właściwą odpowiedź.')
            continue
        else:
            break
    return user_answer

def guessing_game():
    """
    Chooses number until reaching correct value
    :return: guess
    """

    max = 1000
    min = 0
    guess = int((max - min) / 2) + min
    try:
        while True:
            number_input = int(input('Wprowadź liczbę całkowitą od 1 do 1000, a ja ją zgadnę w max 10 próbach: '))
            if number_input > 1000 or number_input < 1:
                print('Liczba spoza zakresu')
                continue
            else:
                print(guess)
                player_response = input(f'Drogi graczu, zgadłem? ').lower()
                proper_response = ('za dużo', 'za mało', 'zgadłeś')

            if player_response not in proper_response:
                print(f'Spodziewam się odpowiedzi:{proper_response}. Wprowadź właściwą odpowiedź')

            if player_response == 'zgadłeś':
                print('Wygrałem')
            elif player_response == 'za dużo':
                guess = int((max - min) / 2) + min
                max = guess
                print(f'Typuję numer: {guess}')
            elif player_response == 'za mało':
                guess = int((max - min) / 2) + min
                min = guess
                print(f'Typuję numer: {guess}')
    except ValueError:
        print('Wprowadzone dane nie są liczbą całkowitą')


if __name__ == '__main__':
    guessing_game()