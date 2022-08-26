# Guessing Game V0.1 2022 - Python by CMarian
from random import randint

print('Hello, welcome to Guess Number v0.1!')
print('Number Pool: 0 - 10 [**in next version, you can change difficulty.**]')

nickname = input('Insert your nickname(for indexing in .txt file, in next version indexing in dtb file):')

print(f'Welcome {nickname}, you can start play now!')
print('Some rules:')
print('-When you lose (not guessing number) you lost 5 score!')
print('-When you win (guessing number) you gain 50 score!')

score = 0
playing = True

while playing == True:
    computer_number = randint(0,10)
    gameloop = True
    while gameloop == True:
        player_number = int(input('Guess number:'))
        if player_number == computer_number:
            score += 20
            print(f'Whoo! You guessed it! Your score now is {score}')
            decision = input('You want to continue playing?(Yes/No):')
            if decision.lower() == 'yes':
                gameloop = False
            else:
                gameloop = False
                playing = False
                print(f'Game Over! Your actual score is {score}')
                file = open('DataBase.txt', 'a')
                file.write(f'{nickname} {score}\n')
                file.close()
        else:
            score -=3
            print(f'Noo! You can try again!')
            print(f'Actual score: {score}')