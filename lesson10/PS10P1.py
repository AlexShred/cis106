#Session 10 Assignment Problems - Advanced Functions --- Alisher Moldoshev

quantity = int(input('How many do you have? '))
price = float(input('How much it cost? '))
discountRate = float(input('How much discount do you have? '))

def totalCost(quantity, price, discountRate):
    fullDisc = (price * quantity) * (discountRate / 100)
    fullTotal = (price * quantity) - fullDisc
    return fullTotal, fullDisc

total, discount = totalCost(quantity, price, discountRate)
print('Quantity:', quantity, 'Price:', price, 'Discount Amount:', discount, 'Discount price:', total)