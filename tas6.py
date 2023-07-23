'''
This code simulates rolling a fair six-sided die
until it lands on the number 6, and records the
number of rolls needed to get a 6. This process
is repeated one million times, and then the average
number of rolls needed to get a 6 is calculated 
and printed.
'''

import random

a = []
for i in range(1000000):
    n = 1
    while (random.randint(1,6) != 6):
        n += 1
    a.append(n)

print (sum(a)/len(a))