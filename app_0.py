weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print("Your weight is  Kg")
else:
    converted = weight / 0.45
    print("Your weigh is  lbs")