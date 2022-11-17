# Python 3: Fibonacci series up to n
n=int(input("Please enter n: "))

a, b = 0, 1
for i in range(n):
    a, b = b, a+b

print(a)