## py script to produce pseudo random numbers
## I used the Linear Congruential Algorithm for this
## more on this here: https://en.wikipedia.org/wiki/Linear_congruential_generator
## seed is current time in epochs

import time

a = 123454321
c = 98765
m = 2**31

def rand():
    obj = time.gmtime(0)
    epoch = time.asctime(obj)
    seed = time.time()
    num = (a * seed + c) % m
    return num

print("Random number you asked for: {0}".format(rand()))