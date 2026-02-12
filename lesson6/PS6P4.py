#Session 6 Assignment Problems – Loop Logic 1 --- ALISHER MOLDOSHEV

answer = input("Do you want to start?\n")
count = 0
allgrosspay = 0

while answer == "yes":
    lastname = input("What is employee last name?\n")
    hoursworked = int(input("How many hours worked?\n"))
    rateofpay = int(input("What is the pay rate?\n"))

    if hoursworked > 40:
        overworked = hoursworked - 40
        grosspay = 40 * rateofpay + overworked * rateofpay * 1.5
    else:
        grosspay = hoursworked * rateofpay

    print(lastname, "gross pay is", grosspay)

    count += 1
    allgrosspay += grosspay

    answer = input("Do you want continue to continue?\n")

print('Count entered employees:', count)
print('All employee gross:', allgrosspay)

if count > 0:
    print('Average pay:', allgrosspay / count)
else:
    print('No pay')