from random import random

values = [random() for i in range(20)]
x = random()

values.sort()#sorts the random list

for j in range(len(values)):
    if values[j] >= x:
        first_index = j#assigns the index to a variable
        break #stops once it finds one greater than the random

print(values)
print(x)
print(first_index)