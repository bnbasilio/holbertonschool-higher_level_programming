#!/usr/bin/python3
import sys
argv = sys.argv[1:]
sum = 0
for element in argv:
    sum += int(element)
if __name__ == "__main__":
    print("{:d}".format(sum))
