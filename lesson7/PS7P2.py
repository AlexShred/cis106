#Moldoshev Alisher ----Session 7 Assignment Problems – Looping Logic 2 and Reading Data from the Keyboard and Files ---

num1 = 1
num2 = 1
print(num1)
print(num2)
i = 2

while i <= 20:
   nextnum = num1 + num2
   print(nextnum)
   num1 = num2
   num2 = nextnum
   i = i + 1
