#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    abm = number % 10
    if abm == 0:
        last_digit = abm
    else:
        last_digit = abm - 10
    print(last_digit)
else:
    last_digit = number % 10
    print (last_digit)
if last_digit > 5:
    print("Last digit of %s is %s and is greater than 5" %(number, last_digit))
elif last_digit == 0:
    print("Last digit of %s is %s and is 0" %(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("Last digit of %s is %s and is less than 6 and not 0" %(number, last_digit))

