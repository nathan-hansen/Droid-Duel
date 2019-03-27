import random
import time
NameIn = 1
def dice():
    playerRoll = random.randint(1,6)
    print('You have rolled', str(playerRoll))

    aiRoll = random.randint(1,6)
    time.sleep(2)
    print('The computer has rolled', str(aiRoll))

    time.sleep(1)

    if playerRoll > aiRoll:
        print('You win!')
    elif playerRoll == aiRoll:
        print("It's a draw!")
    else:
        print('You lose!')

    time.sleep(1)

    print('Would you like to quit the game? Y/N?')
    choice = input()

    if choice == 'Y' or choice == 'y':
        exit()
    elif choice == 'N' or choice == 'n':
        print('Returning to game select...')
        time.sleep(1)
        pass
    else:
        print('Invalid input.  Returning to game select.')

def dice2():
    playerRoll = random.randint(1, 6)
    playerRoll2 = random.randint(1, 6)
    print('You have rolled', str(playerRoll + playerRoll2))

    aiRoll = random.randint(1,6)
    aiRoll2 = random.randint(1,6)
    time.sleep(2)
    print('The computer has rolled', str(aiRoll + aiRoll2))

    time.sleep(1)

    if (playerRoll + playerRoll2) > (aiRoll + aiRoll2):
        print('You win!')
    elif (playerRoll + playerRoll2) == (aiRoll + aiRoll2):
        print("It's a draw!")
    else:
        print('You lose!')

    time.sleep(1)

    print('Would you like to quit the game? Y/N?')
    choice = input()

    if choice == 'Y' or choice == 'y':
        exit()
    elif choice == 'N' or choice == 'n':
        print('Returning to game select...')
        time.sleep(1)
        pass
    else:
        print('Invalid input.  Returning to game select.')

def cointoss():
    print('Heads or Tails?')
    choice = input()

    print('You selected', choice + '.')
    time.sleep(1)
    print('Flipping coin...')

    time.sleep(3)

    flip = random.randint(1, 2)
    if flip == 1:
        print('The coin landed on heads!')
    else:
        print('The coin landed on tails!')
    time.sleep(1)
    if flip == 1 and choice == 'heads' or choice == 'HEADS' or choice == 'Heads':
        print('You win!')
    elif flip == 2 and choice == 'tails' or choice == 'TAILS' or choice == 'Tails':
        print('You win!')
    else:
        print('You lose!')

    print('Would you like to quit the game? Y/N?')
    choice = input()

    if choice == 'Y' or choice == 'y':
        exit()
    elif choice == 'N' or choice == 'n':
        print('Returning to game select...')
        time.sleep(1)
        pass
    else:
        print('Invalid input.  Returning to game select.')

def numgame():
    num = int(random.randint(1, 20))
    lives = 3
    win = 0
    time.sleep(1)
    print('I am thinking of a number between 1 and 20.')
    time.sleep(1)
    print('You need to guess that number.')
    time.sleep(1)
    print('Please enter your first guess.  You have 4 tries.')
    guess = int(input())
    while lives != 0:
        if guess == num and lives >= 0:
            print('Correct!')
            lives = 0
            win = 1
            break
        else:
            print('Nope. Try again.')
            if num > guess:
                print('The number is higher.')
            else:
                print('The number is lower.')
            lives -= 1
            guess = int(input())

    if lives == 0 and win == 1:
        print('Congratulations! You have won! The number was', num)
    elif lives == 0 and win == 0:
        print('Sorry! You have lost. The number was', str(num) + '.')

    print('Would you like to quit the game? Y/N?')
    choice = input()


    if choice == 'Y' or choice == 'y':
        exit()
    elif choice == 'N' or choice == 'n':
        print('Returning to game select...')
        time.sleep(1)
        pass
    else:
        print('Invalid input.  Returning to game select.')


if NameIn == 1:
    print()
    print("What is your name, user?")
    name = input()
    NameIn = 0
    print("Hello,", name + '.')

while True:
    time.sleep(1)
    print()
    print('Enter 1 for dice game with one die.')
    time.sleep(0.5)
    print('Enter 2 for dice game with two dice.')
    time.sleep(0.5)
    print('Enter 3 for coin toss.')
    time.sleep(0.5)
    print('Enter 4 for number game.')
    time.sleep(0.5)
    select = int(input())
    if select == 1:
        print()
        print('Welcome to dice game,', name + '.', 'Press Enter to roll a die.')
        roll = input()
        dice()
    elif select == 2:
        print()
        print('Welcome to dice game 2,', name + '.', 'Press Enter to roll the dice.')
        roll = input()
        dice2()
    elif select == 3:
        print()
        print('Welcome to coin toss,', name + '.',)
        cointoss()
    elif select == 4:
        print()
        print('Welcome to number game,', name + '.')
        numgame()