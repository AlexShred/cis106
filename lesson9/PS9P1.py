#Session 9 Assignment Problems – More on Functions --- Alisher Moldoshev

StartQuestion = input("Do you want start? ").lower()

def nmForecast(month, sales):
    if month in ['Jan', 'Feb', 'Mar']:
        forecast = sales * (1 + 0.1)
        return forecast
    elif month in ['Apr', 'May', 'Jun']:
        forecast = sales * (1 + 0.15)
        return forecast
    elif month in ['Jul', 'Aug', 'Sep']:
        forecast = sales * (1 + 0.2)
        return forecast
    elif month in ['Oct', 'Nov', 'Dec']:
        forecast = sales * (1 + 0.25)
        return forecast

while StartQuestion == 'yes':
    lastName = input("Enter your last name: ")
    month = input("Enter your month: ").strip().title()
    sales = float(input("Enter your sales: "))

    frcst = nmForecast(month, sales)
    print(f"{lastName} monthly sales is: {frcst}")

    StartQuestion = input("Do you want continue? ").lower()