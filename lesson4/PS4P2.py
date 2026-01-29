#Alisher Moldoshev --- 01.29.2026 --- assignment 4

A = 10
B = 20

itemName = input('Enter the item name(A or B): ')
itemQuantity = int(input('Enter the item quantity: '))

if itemName == 'A':
    itemPrice = A
    extendedPrice = itemPrice * itemQuantity
else:
    itemPrice = B
    extendedPrice = B * itemQuantity

print('The extended price is', extendedPrice,
      '\nitem name is ',itemName,
      '\nitem price is ',itemPrice
      )
