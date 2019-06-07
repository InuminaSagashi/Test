#This program is designed to go through a list of numbers and remove items from the list that contain a zero

list = []
for number in range(0, 1000):
    list.append(number)

for list_item in list:
    digit = str(list_item)
    for zero_check in digit:
        int(zero_check)
        if int(zero_check) == 0:
            list.remove(list_item)

print(list)
