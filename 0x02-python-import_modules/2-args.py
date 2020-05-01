#!/usr/bin/python3
import sys
argc = len(sys.argv) - 1
if __name__ == "__main__":
    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc > 0:
        if argc == 1:
            print("{:d} argument:".format(argc))
        if argc > 1:
            print("{:d} arguments:".format(argc))
        i = 1
        argv = sys.argv[1:]
        for element in argv:
            print("{:d}: {}".format(i, element))
            i += 1

