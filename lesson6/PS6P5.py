#Session 6 Assignment Problems – Loop Logic 1 --- ALISHER MOLDOSHEV

answer = input("Do you want to start?\n")
count = 0
alldiscount = 0

while answer == "yes":
    priceitem = float(input("What is price?\n"))
    quantityitem = float(input("What is quantity?\n"))
    extendedprice = priceitem * quantityitem

    if extendedprice > 10000:
        discount = extendedprice * 0.25
    else:
        discount = extendedprice * 0.10

    finalprice = extendedprice - discount

    print("The extended price is:", extendedprice)
    print("The discount is:", discount)
    print("The final price is:", finalprice)

    count += 1
    alldiscount += discount

    answer = input("Do you want continue to continue?\n")

print('Count entered employees:', count)
print('All discount:', alldiscount)