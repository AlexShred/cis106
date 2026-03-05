#Session 9 Assignment Problems – More on Functions --- Alisher Moldoshev

StartQuestion = input("Do you want start? ").lower()


def roomSqF(length, width, height):
        squareFootage = (2 * length * width) + (2 * width * height) + (2 * height * length)
        paintGallon = squareFootage / 50

        return paintGallon

while StartQuestion == "yes":
    length = int(input("Enter the length of the room square: "))
    width = int(input("Enter the width of the room square: "))
    height = int(input("Enter the height of the room square: "))

    roomsqrF = roomSqF(length, width, height)

    print("The paint gallon is", roomsqrF)

    StartQuestion = input("Do you want continue? ").lower()