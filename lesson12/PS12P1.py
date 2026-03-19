#CIS 106 Session 11 Assignment - Strings.docx - Moldoshev Alisher

#https://www.supportyourtech.com/tech/how-to-split-a-word-into-letters-in-python-a-step-by-step-guide/
#https://www.w3schools.com/python/ref_string_split.asp

fullName = input("Full Name: ")

def splitName(fullName):
    firstName = fullName.split()[0]
    lastName = fullName.split()[1]
    return firstName, lastName

firstName, lastName = splitName(fullName)

def frstLetter(firstName, lastName):
    return f"{firstName}, {lastName[0]}"

print(frstLetter(fullName, lastName))
