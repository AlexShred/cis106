#Moldoshev Alisher --- CIS 106 Session 5 Assignment

amountConcertTickets = int(input('Enter the amount concert tickets '))

if amountConcertTickets >= 25:
    pricePerTicket = 50
elif amountConcertTickets >= 10 and amountConcertTickets <= 24:
    pricePerTicket = 60
elif amountConcertTickets >= 5 and amountConcertTickets <= 9:
    pricePerTicket = 70
else:
    pricePerTicket = 75

totalCost = amountConcertTickets * pricePerTicket

print('The number of concert tickets is:', amountConcertTickets,
    '\nThe price per is:', pricePerTicket,
    '\nThe total cost is:', totalCost)