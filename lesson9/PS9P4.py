#Session 9 Assignment Problems – More on Functions --- Alisher Moldoshev

StartQuestion = input("Do you want start? ").lower()
total = 0

def ticketCost(miles):
    if miles >= 30:
        price = 12
    elif miles >= 20:
        price = 10
    elif miles >= 10:
        price = 8
    else:
        price = 5
    return price

while StartQuestion == "yes":
    lastName = input("Enter your last name: ").title()
    miles = float(input("Enter your miles: "))

    ticketTotel = ticketCost(miles)
    print(f"{lastName} ticket totel is: ", ticketTotel)
    total += ticketTotel
    StartQuestion = input("Do you want continue? ").lower()

print("Sum price of all tickets is:", total)