#Moldoshev Alisher --- 01.22.2026 --- CIS 106 Session 3 Assignment Problems – Sequence Logi


#input phase
makeCar = input('What is the make of the car? ')
modelCar = input('What is the model of the car? ')
msrpAmount = float(input('Enter the amount of money: '))
discountPercent = float(input('Enter the discount percent: '))

#process phase
amoountOff = (msrpAmount / 100) * discountPercent
discountPrice = msrpAmount - amoountOff

#output phase   
print('Cars make', makeCar,'model is', modelCar,'discount percent', discountPercent,'amount off', amoountOff,
      'discount price', discountPrice)
