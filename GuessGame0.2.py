# Guessing Game V0.25 2022 - Python by CMarian
from random import randint

def playing_game(add, delete, start, stop):
    nickname = input('Insert your nickname(for indexing in .txt file, in next version indexing in dtb file):')
    print(f'Welcome {nickname}, you can start play now!')
    score = 0
    playing = True
    while playing == True:
        computer_number = randint(start,stop)
        gameloop = True
        while gameloop == True:
            player_number = int(input('Guess number:'))
            if player_number == computer_number:
                score += add
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
                score -=delete
                print(f'Noo! You can try again!')
                print(f'Actual score: {score}')

print('Hello, welcome to Guess Number v0.1!')
difficulty_select = True
while difficulty_select == True:
    difficulty = int(input('You can select dificulty:\n1-Easy\n2-Medium\n3-Hard\n4-Custom'))
    if difficulty == 1:
        difficulty_select = False
        print('Number pool is 0 - 10! For every number guees you gain 20 score, and for a miss you lose 3 score!')
        print('No hints!')
        playing_game(20,3,0,10)
    elif difficulty == 2:
        difficulty_select = False
        print('Number pool is 0 - 25!For every number guess you gain 70 score, and for a miss you lose 5 score!')
        print('No hints!')
        playing_game(60,5,0,25)
    elif difficulty == 3:
        difficulty_select = False
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
    elif difficulty == 4:
        pool_start = int(input('Insert start pool:'))
        pool_stop = int(input('Insert stop pool:'))
        score_win = int(input('Insert win score:'))
        score_lose = int(input('Insert lose score:'))
        difficulty_select = False
        print(f'Number pool is {pool_start} - {pool_stop}! For every number guees you gain {score_win} score, and for a miss you lose {score_lose} score!')
        playing_game(score_win,score_lose,pool_start,pool_stop)
    else:
        print('No difficulty! Please try again')
        difficulty_select = True