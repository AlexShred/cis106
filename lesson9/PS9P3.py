#Session 9 Assignment Problems – More on Functions --- Alisher Moldoshev

StartQuestion = input("Do you want start? ").lower()

def carPrice(make, model, electVeh, msrp):
    if electVeh == "y":
        percent = 0.30
    elif make == "honda" and model == "accord":
        percent = 0.10
    elif make == "toyota" and model == "rav4":
        percent = 0.15
    else:
        percent = 0.05

    discount = msrp * percent
    new_msrp = msrp - discount
    tax = new_msrp * 0.07
    total = new_msrp + tax
    return total

sum_msrp = 0
sum_total = 0

while StartQuestion == "yes":
    make = input("What is your make? ").lower()
    model = input("What is your model? ").lower()
    electVeh = input("Is your car electric vehicle? (y/n) ").lower()
    msrp = float(input("What is your car MSRP? "))

    carTotal = carPrice(make, model, electVeh, msrp)
    print(f"Your car total is: {carTotal}")

    sum_msrp += msrp
    sum_total += carTotal

    StartQuestion = input("Do you want continue? (yes/no) ").lower()

print("Sum of all MSRP:", sum_msrp)
print("Sum of all sales prices:", sum_total)