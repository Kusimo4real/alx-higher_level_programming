#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = number % 10
if number < 0:
    l = (number % 10) - 10
else:
    l = number % 10
if l > 5:
    print("Last digit of %s is %s and is greater than 5" % (number, l))
elif l == 0:
    print("Last digit of %s is %s and is 0" % (number, l))
elif l < 6 and l != 0:
    print("Last digit of %s is %s and is less than 6 and not 0" % (number, l))
