# Hamid Abbaszadeh - Exam 2 (Arrays)

names = ['Ali','Babak','Jalal','Naser','Elham','Sara','Fatemeh','Radin','John','Leo']
ages  = [20,12,35,8,24,18,38,6,34,41]

#print(names)
#print(ages)


# A- Max and Min
print("======= A : Max and Min =======")

age_max = max(ages)
age_min = min(ages)
oldest_index = ages.index(age_max)
youngest_index = ages.index(age_min)

print(f'Oldest person is {names[oldest_index]} with {age_max} years old.')
print(f'Youngest person is {names[youngest_index]} with {age_min} years old.')


# B- Sorting

tmp_ages = ages[:]
tmp_ages.sort(reverse=True)
new_ages = []
for x in range(len(tmp_ages)):
    if x%2:
        new_ages.insert(0,tmp_ages[x])
    else:
        new_ages.append(tmp_ages[x])

print("\n\n\n======= B: Sorting =======")
print(new_ages)



# C- Find by name
print("\n\n\n======= C: Find by Name =======")


name = input("Please enter a name: ")
f = False
for i in range(10):
    if name == names[i]:
        print(f'{name} is {ages[i]} years old.')
        f = True
        break
if not f : print(f'Sorry! We cannot find any {name} in our list.')
        

# D- Circle list
print("\n\n\n======= D: Circle  List =======")

print(ages)

n = int(input("Please enter N: "))

for _ in range(n):
    tmp = ages[0]
    ages.pop(0)
    ages.append(tmp)

print(ages)