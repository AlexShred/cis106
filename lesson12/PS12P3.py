#CIS 106 Session 11 Assignment - Strings.docx - Moldoshev Alisher

#https://www.geeksforgeeks.org/python/python-removing-unwanted-characters-from-string/

import re

enterLine = input("Enter the line: ")


def processLine(enterLine):
    items = re.split(r'[,\s]+', enterLine)

    for item in items:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', item)

        if cleaned:
            print(cleaned)


processLine(enterLine)