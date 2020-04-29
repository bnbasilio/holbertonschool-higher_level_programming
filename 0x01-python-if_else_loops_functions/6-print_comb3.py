#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if i == 0 and j == 1:
            print("{:d}{:d}".format(i, j), end='')
        elif j > i:
            print(", {:d}{:d}".format(i, j), end='')
        elif i == 8 and j == 9:
            print(", {:d}{:d}".format(i, j))
