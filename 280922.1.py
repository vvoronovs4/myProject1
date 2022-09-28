if __name__ == '__main__':
    one = ('name','is', 'my')
    two = '{2} {0} {1}'.format(*one).capitalize()
    print('{} {}'.format(two, 'Vladialvs'))