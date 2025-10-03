########################## input numbers here #########################

groupOrder = 2^n
modBase = m

base = 1
coefficient = (1*1 % modBase) * (1*1 % modBase) % modBase
print(coefficient)

########################## group elements #########################

def myGCD(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

elementList = []
i = 1
while (i < modBase):
    if (myGCD(i,modBase)==1):
        elementList += [i]
    i += 1
print(elementList)
print(len(elementList))

########################## order 2 elements #########################

order2Elements = []
for i in range(1,modBase):
    check = (i*i%modBase)
    if check == 1:
        order2Elements += [i]
print("Elements of order 2:")
print(order2Elements)

########################## cyclic subgroups #########################

modList = []
element = base
modList += [base]
i = 1
while (element != 1):
    element = element * base % modBase
    modList += [element]
    i += 1
print(modList)
print(len(modList))

########################## products of cyclic subgroups #########################

productList = []
count = 0
while (count < len(modList)):
    factor = modList[count]
    product = factor*coefficient % modBase
    productList += [product]
    count += 1
print(productList)
print(len(productList))




