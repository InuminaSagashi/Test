import numpy
import math

list = []
for number1 in range(1000, 10000):
    if math.sqrt(number1).is_integer():
        list.append(number1)

#All of the numbers in the range 1000 to 9999 that are perfect squares have been added to the list. There are 68 items


for number2 in list:
    if (number2 / 10).is_integer():
        list.remove(number2)

#The same set of numbers that are divisible by 10 have been removed. There are now 62 items; not exactly necessary

for list_item in list[0:62]:
    digit = str(list_item)
    for zero_check in digit:
        if int(zero_check) == 0:
            list.remove(list_item)

print("\n")

for list_item in list [0:62]:
    print(list_item)