#Alisher Moldoshev --- 01.29.2026 --- assignment 4

quantityItems = int(input('Enter the number of items: '))

if quantityItems >= 1000:
    unitPrice = 3
else:
    unitPrice = 5

extendedPrice = quantityItems * unitPrice
taxPrice = extendedPrice * 0.07
totalPrice = extendedPrice + taxPrice

print('The unit price is', unitPrice,
    '\nThe total price is', totalPrice,
    '\nThe tax is', taxPrice,
    '\nThe extended price is', extendedPrice)
