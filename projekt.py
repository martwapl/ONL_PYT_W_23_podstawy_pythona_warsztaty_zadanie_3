def user_input():
    """
    Return proper value provided by user
    :rtype str
    :return:value provided by user from ['za mało', 'za dużo', 'wygrałeś']
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

    input('Wprowadź liczbę od 1 do 1000. Odgadnę ją maksymalnie za 10 podejściem: ')
    min_number = 0
    max_number = 1000
    user_answer = ''
    while user_answer != 'wygrałeś':
        guess = (max_number - min_number) // 2 + min_number
        print(f'Typuję numer: {guess}')
        user_answer = user_input()
        if user_answer == 'za dużo':
            max_number = guess
        elif user_answer == 'za mało':
            min_number = guess
    print('Zgadłem')

if __name__ == '__main__':
    guessing_game()