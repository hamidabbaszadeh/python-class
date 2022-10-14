import random

l = 100000
count = 0

for i in range(l):
    s = set()
    for j in range(23):
        a = random.randint(1, 365)
        if a in s:
            count += 1
            break
        else:
            s.add(a)
    
print(count/l * 100)