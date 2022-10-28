balance = 900


def Withdrawal(amount):
    if balance < amount:
        print('You do not have enough money')
    elif amount > 700:
        print('Daily limit exceeded')
    else:
        print('Success')


def Deposit(amount):
    if amount >= 10000:
        print('Need to register sum in VID')
    else:
        print('Success')


if __name__ == '__main__':
    Withdrawal(1000)
    Withdrawal(900)
    Withdrawal(500)
    Deposit(10001)
    Deposit(5000)
