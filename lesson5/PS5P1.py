#Moldoshev Alisher --- CIS 106 Session 5 Assignment

quantity = int(input('How many widgets do you need?'))


if quantity > 10000:
    price = 10
elif quantity <= 10000 and quantity >= 5000:
    price = 20
elif quantity < 5000:
    price = 30
else:
    print('Wrong value')

totalAmount = (quantity * price) + (((quantity * price) * 0.07))


print('The extented price is:', quantity * price,
    '\nThe tax amount is:', (quantity * price) * 0.07,
    '\nThe total cost is:', totalAmount)