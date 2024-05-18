#!/usr/bin/python3
"""
    a program that prints the resulr of the addition of all arguments

"""
if __name__ == "__main__":
    import sys
    total = 0
    n = len(sys.argv[1:])
    if n == 0:
        print("{}".format("0"))
    else:
        for i in range(1, n+1):
            total += int(sys.argv[i])
        print("{}".format(total))
