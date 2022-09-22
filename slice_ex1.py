if __name__ == '__main__':
    our_string = 'My name is something must go here'
    result = our_string[0:10]
    name = 'Konstantins'
    sliced_text = slice(10)
    print( '{} {}'.format(our_string[sliced_text], name))