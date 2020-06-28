# Hamid Abbaszadeh - Exam - 5

import random
import statistics


randomlist = []

for _ in range(20):
    n = random.randint(1,1500)
    randomlist.append(n)

print(randomlist)

q = 0 
for n in randomlist:
    if n%10 == 3 :
        q += 1


print("\nNumber with 3 in frist: ",q)

x = sum(randomlist) / len(randomlist)
print("\nMean of this list is:",x)

y = statistics.median(randomlist)
print("\nMedian of this list is:",y)