#Session 8 Assignment Problems - Introduction to Functions ---- Alisher Moldoshev

startq = input('Do you want start?')

summ = 0

def total(quantity, price):
    sum = quantity * price

    if sum > 10000:
        sum = sum * 0.9

    return sum

while startq == 'yes':

    quantity = int(input('Enter the quantity of items: '))
    price = float(input('Enter the price of items: '))

    result = total(quantity, price)
    print("Quantity:", quantity, "Price:", f"{price:.2f}", "Total:", f"{result:.2f}")
    summ += result

    startq = input('Do you want continue?')

print("Total sum:", f"{summ:.2f}")
