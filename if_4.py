def colour(number):
    if 380 <= number <= 449:
        print('Violet')
    elif 450 <= number <= 494:
        print('Blue')
    elif 495 <= number <= 569:
        print('Green')
    elif 570 <= number <= 589:
        print('Yellow')
    elif 590 <= number <= 619:
        print('Orange')
    elif 620 <= number <= 750:
        print('Red')
    else:
        print('Invisible light')


if __name__ == '__main__':
    colour(1)
