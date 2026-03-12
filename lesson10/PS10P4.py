#Session 10 Assignment Problems - Advanced Functions --- Alisher Moldoshev

bowlerName = input('Enter bowler lastname: ').capitalize()
gameOne = int(input('What is game 1 score? '))
gameTwo = int(input('What is game 2 score? '))
gameThree = int(input('What is game 3 score? '))
handicap = int(input('What is handicap score? '))

def scoregame(gameOne, gameTwo, gameThree, handicap):
    AverageScore = (gameOne + gameTwo + gameThree) / 3
    scoreHandicap = (AverageScore + handicap) / 3
    return AverageScore, scoreHandicap

AverageScoreGame, ScoreHandicapGame = scoregame(gameOne, gameTwo, gameThree, handicap)

print("Bowler's name: ", bowlerName, f"Average score: {AverageScoreGame:.2f}" , f"Handicap score: {ScoreHandicapGame:.2f}")