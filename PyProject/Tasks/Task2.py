#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a1 = int(input("Введите координату а1: "))
    b1 = int(input("Введите координаду b1: "))
    c1 = int(input("Введите координату c1: "))
    a2 = int(input("Введите координату а2: "))
    b2 = int(input("Введите координату b2: "))
    c2 = int(input("Введите координату c2: "))

    if a1 / a2 == b1 / b2:
        if c1 / a1 == c2 / a2:
            print("Прямые совпадают")
        else:
            print("Прямые параллельны")
    else:
        x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
        y = (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)
        print("Точка пересечения: (",x,",",y,")")
    
