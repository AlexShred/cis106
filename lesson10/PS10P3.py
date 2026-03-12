#Session 10 Assignment Problems - Advanced Functions --- Alisher Moldoshev

salesName = input('Enter salesperson last name: ').capitalize()
sales = float(input('Enter sales price: '))

def commission(sales):
    if sales > 100000:
        comPrice = sales * 0.1
    else:
        comPrice = sales * 0.05

    nextYear = sales * 1.05

    return comPrice, nextYear

comAmount, nextyear = commission(sales)

print('Salesperson last name:', salesName, f'Commision is {comAmount}', f'Next year is {nextyear}')