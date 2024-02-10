dec = 9
count = 0
for i in range (1, 9):
    for j in range (0, 9):
        dec += 1
        sum = i + j
        if sum + sum**2 == dec:
            count += 1
print("Всего существует", dec, "таких чисел")