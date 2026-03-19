#CIS 106 Session 11 Assignment - Strings.docx - Moldoshev Alisher

#https://stackoverflow.com/questions/1546226/is-there-a-simple-way-to-remove-multiple-spaces-in-a-string
#https://www.w3schools.com/python/python_howto_reverse_string.asp

import re

lineText = input("Line Text: ")

def deleteDuplSpaces(lineText):
    lineText1 = re.sub(r'\s+', ' ', lineText)
    return lineText1

def reverse(lineText1):
  return lineText1[::-1]

print(reverse(deleteDuplSpaces(lineText)))