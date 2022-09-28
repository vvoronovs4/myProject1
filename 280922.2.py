if __name__ == '__main__':
    one = 't1234h1234i1234saaaaiaaaasbbbbm1234yaaaapbbbbabbbbsaaaas1234'
    one_corrected = one.replace('1234', '')
    one_corrected_2 = one_corrected.replace('aaaa', '')
    one_corrected_3 = one_corrected_2.replace('bbbb', '')
    slice1 = slice(0, 4)
    slice2 = slice(4, 6)
    slice3 = slice(6, 8)
    slice4 = slice(8, 12)
    two = '{} {} {} {}'.format(one_corrected_3[slice1].capitalize(), one_corrected_3[slice2], one_corrected_3[slice3], one_corrected_3[slice4])
    print(two)

