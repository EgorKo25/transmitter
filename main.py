import matplotlib.pyplot as plt
import random as rd
import numpy as np

# Поиск старшего бита
def head_bit(value):

    bit_num = 31
    cmp_val = 1 << bit_num

    while value < cmp_val:
        cmp_val >>= 1
        bit_num -= 1

    return bit_num


"""
def polynomial_division_mod(dividend, divider):

    m = head_bit(divider)

    k = head_bit(dividend) - m

    if k < 0:
        return dividend

    while k >= 0:
        tmp = divider << k

        
        k = head_bit(dividend) - m
    return dividend
"""
# Деление полиномов
def polynomial_division(dividend, divider):
    m = head_bit(divider)
    k = head_bit(dividend) - m

    while True:

        if k < 0:
            return dividend

        tmp = divider << k
        dividend ^= tmp
        k = head_bit(dividend) - m


# Генерация случайного вектора ошибок
def error_vector_creater(length, p):
    error = 0

    for j in range(length):
        new_e = rd.random()

        if new_e  < (p / 100):
            error <<= 1
            error += 1
            continue

        error <<= 1

    return error

# Построение графика
def graph_creater(x, y):

    plt.figure(label="Иллюстрация изменения вероятности")

    plt.plot(x, y, label="Изменение вероятности ошибки", mec="b")

    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    g = input("Введите полином: ")
    len_encode_sequence = int(input("Введите длину кодируемой последовательности: "))

    

    g_len = int(input("Введите длину полинома: "))
    g = int(g)
    g_pow = g_len -1
    
    k = g_pow + g_len

    low_border = 2 ** (len_encode_sequence - 1)
    high_border = (2 ** len_encode_sequence) - 1

    pe = 0 
    array_vector = []
    p = 0

    for p in range(101):
        print('Completed: {}%'.format(p), end='\r')
        for i in range(10000):
            encoded_msg = rd.randint(low_border, high_border)

            mxxr = encoded_msg *  (2 ** g_pow)
            c = polynomial_division(mxxr, g)

            sended_msg = mxxr + c
            
            ver = 1
            error_vector = error_vector_creater(k, p)

            goted_msg = sended_msg ^ error_vector

            syndrom = polynomial_division(goted_msg, g)ага

            if syndrom == 0 and error_vector > 0:
                pe += 1

        pe /= 10000

        array_vector.append(pe)

    p = [i/100 for i in range(0, 101)]

    graph_creater(p, array_vector)


main()