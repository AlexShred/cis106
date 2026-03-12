#Session 10 Assignment Problems - Advanced Functions --- Alisher Moldoshev

quantity = int(input('Enter quantity of sales: '))
unitPrice = int(input('Enter unit price: '))

totalItem = 0
tax = 0

def total(quantity, unitPrice):
    global totalItem, tax
    totalItem = quantity * unitPrice
    tax = totalItem * 0.07

total(quantity, unitPrice)
print(f"Total price is {totalItem}", f"Tax is {tax}")