def fly_forward():
    print('You moved forward')


def fly_left():
    print('You moved left')


def fly_right():
    print('You moved right')


def game_over(my_name):
    print('Game over ' + my_name)


def shoot(somenumber):
    hp_enemy = 1000
    print('You dealt damage of {}'.format(somenumber))
    hp_enemy -= somenumber
    return hp_enemy


if __name__ == '__main__':
    fly_left()
    print(shoot(200))
    fly_forward()
    fly_right()
    game_over('Joe Biden')
