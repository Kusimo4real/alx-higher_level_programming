#!/usr/bin/python3
"""
    a program that prints the number of and the list of its arguments.
"""
if __name__ == "__main__":
    import sys
    n = len(sys.argv[1:])
    if n == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(n))

    for i in range(1, n+1):
        print("{}: {}".format(i, sys.argv[i]))
