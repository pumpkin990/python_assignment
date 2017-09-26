import math
num = int(input("Enter a number..."))
total = 0
for i in range(0,num+1):
    if i % 2 == 1:
        total = total + math.pow(i,2)
print(total)
