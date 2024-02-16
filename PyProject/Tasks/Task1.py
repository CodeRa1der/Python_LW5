#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    exams = int(input("Сколько экзаменов мы сдали? "))

    if exams > 20:
        print("Слишком много экзаменов!")
    elif exams == 1:
        print("Мы успешно сдали 1 экзамен")
    elif exams >= 2 and exams <= 4:
    print("Мы успешно сдали", exams, "экзамена")
    elif exams >= 5:
    print("Мы успешно сдали", exams, "экзаменов")
