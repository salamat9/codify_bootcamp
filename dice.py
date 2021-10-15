import random


print('Dice Game!')


def mix(player):
    tries = 5
    question = player + ' type mix or anything: '
    while True:
        if tries == 0:
            print(player + ' lost!')
            exit()
        if input(question) == 'mix':
            tries -= 1
            print(f'dices is mixed! You have tries {tries}')
        else:
            break


def dice(player):
    """
    функция возвращает сумму двух костей
    """
    mix(player)
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    print(f'first dice is {first_dice}.')
    print(f'second dice is {second_dice}.')
    return first_dice + second_dice


score_player_1 = 0
score_player_2 = 0
for i in range(3):
    score_player_1 += dice('first player\'s turn\n')
    score_player_2 += dice('second player\'s turn\n')

print('player 1', score_player_1)
print('player 2', score_player_2)
if score_player_1 != score_player_2:
    print('something')

print(score_player_1)
print(score_player_2)


