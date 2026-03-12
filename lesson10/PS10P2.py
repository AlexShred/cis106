#Session 10 Assignment Problems - Advanced Functions --- Alisher Moldoshev

studentName = input('Enter student name: ').capitalize()
scoreOne = int(input('What is student score 1? '))
scoreTwo = int(input('What is student score 2? '))
scoreThree = int(input('What is student score 3? '))

def totalScore(scoreOne, scoreTwo, scoreThree):
    averageScore = (scoreOne + scoreTwo + scoreThree) / 3
    totalPoints = scoreOne + scoreTwo + scoreThree
    return totalPoints, averageScore

total, average = totalScore(scoreOne, scoreTwo, scoreThree)

print('Student name is', studentName ,f'The average score is: {average}', f'The total points is: {total}')