#Session 9 Assignment Problems – More on Functions --- Alisher Moldoshev

StartQuestion = input("Do you want start? ").lower()

totalMarket = 0
totalAssessed = 0

def assessedValue(marketValue, county):
    county = county.lower()

    if county == "cook":
        assessedValPer = 0.90
    elif county == "dupage":
        assessedValPer = 0.80
    elif county == "mchenry":
        assessedValPer = 0.75
    elif county == "kane":
        assessedValPer = 0.60
    else:
        assessedValPer = 0.70

    totalValue = marketValue * assessedValPer
    return totalValue

while StartQuestion == "yes":
    county = input("What county do you want? ")
    marketValue = float(input("What is the market value? "))

    assValTotal = assessedValue(marketValue, county)

    print("Assessed value is:", assValTotal)

    totalMarket += marketValue
    totalAssessed += assValTotal

    StartQuestion = input("Do you want continue? ").lower()

print("Sum of all market values is:", totalMarket)
print("Sum of all assessed values is:", totalAssessed)