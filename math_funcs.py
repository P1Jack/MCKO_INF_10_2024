def normalization(number):
    before = bin(abs(int(number)))[2:]
    after = ''
    a = float('0.' + str(number).split('.')[1])
    while a != 1.0:
        a *= 2
        tmp = 1 if a >= 1.0 else 0
        if a > 1.0:
            a -= float(int(a))
        after += str(tmp)
    return before, after


def number5(number, d=127, format=32, base='16'):
    before, after = normalization(number)
    head = '1' if number < 0 else '0'
    p = bin(6 - before.index('1') + d)[2:].rjust(8, '0')
    tail = (before + after)[1:].ljust(format - 1 - 8, '0')
    computer = head + p + tail
    print(base)
    if base == '2':
        print(computer)
        return computer
    elif base == '8':
        print(oct(int(computer, 2))[2:])
        return oct(int(computer, 2))[2:]
    elif base == '10':
        print(str(int(computer, 2)))
        return str(int(computer, 2))
    elif base == '16':
        print(hex(int(computer, 2))[2:].upper())
        return hex(int(computer, 2))[2:].upper()


def to_dec(number, base):
    degree = len(str(int(number.split(',')[0]))) - 1
    dec = 0
    number = number.replace(',', '')
    for i in range(len(number)):
        dec += int(number[i]) * (base ** degree)
        degree -= 1
    return dec


def number1(number1, base1, number2, base2, res_base, sign):
    dec_number1 = to_dec(number1, base1)
    dec_number2 = to_dec(number2, base2)
    E = int(eval(f'{dec_number1} {sign} {dec_number2}'))
    if res_base == '2':
        print(bin(E)[2:])
        return bin(E)[2:]
    elif res_base == '8':
        print(oct(E)[2:])
        return oct(E)[2:]
    elif res_base == '10':
        print(E)
        return str(E)
    elif res_base == '16':
        print(hex(E)[2:].upper())
        return hex(E)[2:].upper()


# print(number1('1011,01', 2, '24,6', 8, '16', '+'))
