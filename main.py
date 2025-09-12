def myGCD(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

########################## input numbers here #########################

groupOrder = 2^n
modBase = m

base = # % modBase
coefficient = (1 * 1 % modBase) * (1 * 1 % modBase) % modBase
print(coefficient)

########################## group information #########################

elementList = []
i = 1
while (i < modBase):
    if (myGCD(i,modBase)==1):
        elementList += [i]
    i += 1
print(elementList)
print(len(elementList))

########################## base #########################

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

########################## product list #########################

productList = []
count = 0
while (count < len(modList)):
    factor = modList[count]
    product = factor*coefficient % modBase
    productList += [product]
    count += 1
print(productList)
print(len(productList))
