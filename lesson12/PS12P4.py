#CIS 106 Session 11 Assignment - Strings.docx - Moldoshev Alisher

# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://www.w3schools.com/python/python_strings_slicing.asp

lineText = input("Enter the line: ")
numCharsPerLine = int(input("Enter the number of character(s): "))
numLines = int(input("Enter the number of lines: "))
scrollDirection = input("Enter the scroll direction: ").lower()

def shiftLeft(text):
    if text == "":
        return text
    return text[1:] + text[0]

def shiftRight(text):
    if text == "":
        return text
    return text[-1] + text[:-1]

def printScroll(lineText, numCharsPerLine, numLines, scrollDirection):
    currentText = lineText

    for i in range(numLines):
        print(currentText[:numCharsPerLine])

        if scrollDirection == "left":
            currentText = shiftLeft(currentText)
        elif scrollDirection == "right":
            currentText = shiftRight(currentText)
        else:
            print("Invalid direction")
            break

printScroll(lineText, numCharsPerLine, numLines, scrollDirection)