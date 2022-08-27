# Guessing Game V0.2 2022 - Python by CMarian
from random import randint

print('Hello, welcome to Guess Number v0.1!')
difficulty = int(input('You can select dificulty:\n1-Easy\n2-Medium\n3-Hard'))
if difficulty == 1:
    print('Number pool is 0 - 10! For every number guees you gain 20 score, and for a miss you lose 3 score!')
    print('No hints!')
    nickname = input('Insert your nickname(for indexing in .txt file, in next version indexing in dtb file):')
    print(f'Welcome {nickname}, you can start play now!')
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
elif difficulty == 2:
    print('Number pool is 0 - 25!For every number guess you gain 70 score, and for a miss you lose 5 score!')
    print('No hints!')
    nickname = input('Insert your nickname(for indexing in .txt file, in next version indexing in dtb file):')
    print(f'Welcome {nickname}, you can start play now!')
    score = 0
    playing = True
    while playing == True:
        computer_number = randint(0,25)
        gameloop = True
        while gameloop == True:
            player_number = int(input('Guess number:'))
            if player_number == computer_number:
                score += 70
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
                score -=5
                print(f'Noo! You can try again!')
                print(f'Actual score: {score}')
elif difficulty == 3:
    print('Number pool is 0 - 100! For every number guess you gain 200 score, and for a miss you lose 7 score!')
    print('When you are too far from the number, you recive a message where you are warned!')
    nickname = input('Insert your nickname(for indexing in .txt file, in next version indexing in dtb file):')
    print(f'Welcome {nickname}, you can start play now!')
    score = 0
    playing = True
    while playing == True:
        computer_number = randint(0,100)
        gameloop = True
        while gameloop == True:
            player_number = int(input('Guess number:'))
            if player_number == computer_number:
                score += 200
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
                if computer_number < player_number:
                    gap = player_number - computer_number
                else:
                    gap = computer_number - player_number
                score -=7
                print(f'Noo! You can try again!')
                if gap > 25:
                    print('Too far, you are about 25+ positions away!')
                print(f'Actual score: {score}')
else:
    print('No dificulty! Game Over!')