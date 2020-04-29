#!/usr/bin/python3
for i in range(8):
    for j in range(1, 9):
        if i == 0 and j == 1:
            print("01", end='')
        elif j > i:
            print(", {:d}{:d}".format(i, j), end='')
print(", 89")
