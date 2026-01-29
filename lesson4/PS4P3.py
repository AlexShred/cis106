#Alisher Moldoshev --- 01.29.2026 --- assignment 4

amountBook = int(input('How many books do you want to buy? '))
costPerBook = int(input('How much they are cost? '))

totalAmount = amountBook * costPerBook

if totalAmount > 50:
    print('Shipping is free, your total cost is', totalAmount)
else:
    print('Your total cost is plus shipping cost 25$', totalAmount + 25)
