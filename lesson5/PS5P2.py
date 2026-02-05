#Moldoshev Alisher --- CIS 106 Session 5 Assignment

partNumber = input('Enter a part number: ')
quantity = int(input('Enter an item: '))

if partNumber =='10' or partNumber =='55':
    unitCost = 1
elif partNumber =='80' or partNumber =='75':
    unitCost = 3
elif partNumber == '99':
    unitCost = 2
else:
    unitCost = 5

totalCost = quantity * unitCost

print('The total cost is:', totalCost,
    '\nThe unit cost is:', unitCost,
    '\nThe part number is:', partNumber)
