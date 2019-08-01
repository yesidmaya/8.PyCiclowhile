# -*- coding: utf-8 -*-

def my_count(number):
    i = 0
    while i < number:
        a = print(i)
        i += 1



if __name__ == "__main__":
    number = int(input('Digite un numero: '))

    result = my_count(number)
    print(result)