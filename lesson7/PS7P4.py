#Moldoshev Alisher ----Session 7 Assignment Problems – Looping Logic 2 and Reading Data from the Keyboard and Files ---



with open("iteminfo.txt", "w") as file:
    cont = "yes"

    while cont == "yes":
        item = input("Enter item name: ")
        quantity = float(input("Enter quantity: "))
        price = float(input("Enter price: "))

        file.write(f"{item}\n")
        file.write(f"{quantity}\n")
        file.write(f"{price}\n")

        cont = input("Add another item? (yes/no): ").strip().lower()



allprice = 0
ordersnum = 0

with open('iteminfo.txt', 'r') as file:
    while True:
        item = file.readline().strip()
        if not item:
            break

        quantity = float(file.readline().strip())
        price = float(file.readline().strip())

        total = quantity * price

        print(f"Item: {item}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")
        print(f"Extended Price: {total}\n")

        allprice += total
        ordersnum += 1

    average = allprice/ordersnum if ordersnum > 0 else 0

    print(f"Total of all extended prices: {allprice}")
    print(f"Number of orders: {ordersnum}")
    print(f"Average order: {average}")