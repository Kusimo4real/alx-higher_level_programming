#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lw = number % 10
if number < 0:
    lw = (number % 10) - 10
else:
    lw = number % 10
if lw > 5:
    print("Last digit of %s is %s and is greater than 5" % (number, lw))
elif lw == 0:
    print("Last digit of %s is %s and is 0" % (number, lw))
elif lw < 6 and lw != 0:
    print("Last digit of %s is %s and is less than 6 and not 0" % (number, lw))
