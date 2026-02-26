#Session 8 Assignment Problems - Introduction to Functions ---- Alisher Moldoshev

startq = input('Do you want to continue? (yes/no): ')

playersQuan = 0

def battingAverage(hitsquantity, batsquantity):
    batAverage = hitsquantity / batsquantity
    return batAverage

while startq == 'yes':
    playerName = input('Enter the player name: ')
    hitsquantity = int(input('Enter the number of hits: '))
    batsquantity = int(input('Enter the number of bats: '))

    result = battingAverage(hitsquantity, batsquantity)

    print(playerName, f'the batting average is: {result}')
    startq = input('Do you want to continue? (yes/no): ')
    playersQuan +=1

print('Total players ', playersQuan)