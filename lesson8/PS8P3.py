#Session 8 Assignment Problems - Introduction to Functions ---- Alisher Moldoshev

contq = input('Do you want to continue? (yes/no): ')

quant = 0

def milesPerGalon(milesTraveled, gallonsUsed):
    if gallonsUsed == 0:
        return 0
    else:
        perMile = milesTraveled / gallonsUsed
        return perMile

while contq == 'yes':
    milesTraveled = float(input('Enter the miles traveled: '))
    gallonsUsed = float(input('Enter the gallons used: '))
    cityName = input('Enter the city name: ')

    quant +=1
    result = milesPerGalon(milesTraveled, gallonsUsed)

    print(f"{cityName} - Miles: {milesTraveled}, MPG: {result:.2f}")

    contq = input('Do you want to continue? (yes/no): ')

print('Total trips: ', quant)

