# Hamid Abbaszadeh - Exam 2


# INPUT Products details
products = []
n = 0
while True:
    print("Please enter product details:\n================")
    code  = int(input("Enter a code (0 to exit): "))
    if code == 0 : break
    name  = input("Enter name : ")
    color = input("Enter color: ")
    qty   = int(input("Enter qty  : "))
    price = int(input("Enter price: "))
    products.append([code,name,color,qty,price])
    n += 1
    print("\n")


# INPUT filename
fname = input("\nPlease enter filename to save product: ")
#while True:
#    dname = input("Please select a drive [C: or D:] : ")
#    if dname.capitalize() == "C" or dname.capitalize() == "D": break

#filename = dname+ ":\\" + fname + ".txt"
filename = fname

# SAVE data in File
f = open(filename, "w")

for product in products:
    for item in product:
        f.write(str(item)+'\t')
    f.write('\n')
f.close()


# A- COLOR
print("\n\n\nCOLOR\n================")

colorname = input("Please enter a color: ")

color_qty = 0
for product in products:
    if colorname == product[2]:
        color_qty += 1
print(f'There is {color_qty}  product(s) in {colorname} color')
    

# B- TOTAL
print("\n\n\nTOTAL\n================")
print(f'{n} product(s) are saved in {filename}')