#Session 6 Assignment Problems – Loop Logic 1 --- ALISHER MOLDOSHEV

answer = input("Do you want start cycle?\n")
count = 0

while answer == "yes":
    lastname = input("Enter last name?\n")
    scorefrst = int(input("Enter score first?\n"))
    scorescnd = int(input("Enter score second?\n"))

    averagescore = (scorefrst + scorescnd) / 2

    print( lastname ,"the average score is:", averagescore)
    count += 1

    answer = input("Do you want continue to continue?\n")

print("Number of students entered", count)