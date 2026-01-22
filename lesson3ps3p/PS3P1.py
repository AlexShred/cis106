#Moldoshev Alisher --- 01.22.2026 --- CIS 106 Session 3 Assignment Problems – Sequence Logi

#input phase
stockTicker = input('Enter the stock ticker symbol: ')
numberOfShare = int(input('Enter the number of shares: '))
costPerShare = float(input('Enter the cost per share: '))

#process phase
amountInvested = numberOfShare * costPerShare


#output phase
print('Your total amount invested is ', amountInvested, 'to the ', stockTicker)

