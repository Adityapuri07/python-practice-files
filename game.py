import random
import os

fruit_dict = {
    1: 'Apple',
    2: 'Banana',
    3: 'Orange',
    4: 'Mango',
    5: 'Pineapple',
    6: 'Strawberry',
    7: 'Watermelon',
    8: 'Grape',
    9: 'Kiwi',
    10:'Peach'
}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def game(level):
    total_points = 0
    while True:
        print('Remember the Fruits Name with their corresponding numbers :')
        selected_fruits = {}
        keys_for_selection = random.sample(list(fruit_dict.keys()), level)
        print(keys_for_selection)
        for key in keys_for_selection:
            print(f"{key} {fruit_dict[key]}")
            selected_fruits[key] = fruit_dict[key]
        res = input(' Ready for test enter Yes/No : ')
        if res == 'yes' or res == 'Yes':
            clear_terminal()
            random_fruit_key = random.choice(list(selected_fruits.keys()))
            random_fruit = selected_fruits[random_fruit_key]
            fruit_id = input(f'What was the number of {random_fruit}: ')
            if int(fruit_id) == random_fruit_key:
                print('Correct answer!')
                total_points += 1
                print(f'You have earned {total_points} points')

                cho = int(input('Press 1 to continue or 2 to exit: '))
                if cho == 1:
                    continue
                elif cho == 2:
                    print('Thanks !!')
                    exit()
            else:
                print('Wrong answer! Please try again.')
                continue
        elif res == 'no' or res == 'No':
            print('Thanks !!')
            exit()
        elif res == "":
            print('Please Choose any option')
            continue


print('/---------WELCOME TO THE GAME -----------/')
print('Please choose any number:')
print('Press 1 for Easy level')
print('Press 2 for Medium level')
print('Press 3 for Hard level')

n = int(input('Choose the level you want to play: '))
if n == 1:
    print('------ You selected Easy level ----')
    game(3)
elif n == 2:
    print('------ You selected Medium level ----')
    game(6)
elif n == 3:
    print('------ You selected Hard level ----')
    game(10)
else:
    print('Invalid selection!')

