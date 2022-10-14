# Python
n = int(input("Please enter a number: ")


a, b = 0, 1
for i in range(n):
    a, b = b, a+b

for x in range(1,n+1):
    s = 0
    for y in range(1,x//2 + 1):
        if not x%y:
            s += y 
    if x == s:
        print(x)