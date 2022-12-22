def guessing_game():
    max = 1000
    min = 0
    guess = int((max - min) / 2) + min
    while True:
        number_input = int(input('Wprowadź liczbę od 1 do 1000, a ja ją zgadnę w max 10 próbach: '))
        if number_input > 1000 or number_input < 1:
            print('Liczba spoza zakresu')
            continue
        else:
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

if __name__ == '__main__':
    guessing_game()