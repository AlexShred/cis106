#Alisher Moldoshev --- 01.29.2026 --- assignment 4

nameCustomer = input('Enter your name: ')
costOfAppliance = int(input('Enter your cost of appliance: '))

if costOfAppliance >= 1000:
    totalAmount = costOfAppliance + (costOfAppliance * 0.10)
else:
    totalAmount = costOfAppliance + (costOfAppliance * 0.05)

print(nameCustomer.capitalize(), 'your total cost is', totalAmount, 'cost of the warrantee ',costOfAppliance * 0.10)
