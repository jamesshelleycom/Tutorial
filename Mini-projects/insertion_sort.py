import random

working_list = []
for num in range(random.randint(5, 15)):
    working_list.append(random.randint(1, 999))

print("Before sort:", working_list)

for num in range(1, len(working_list)):
    current_position = num
    while current_position > 0 and working_list[current_position - 1] > working_list[current_position]:
        temp = working_list[current_position]
        working_list[current_position] = working_list[current_position - 1]
        working_list[current_position - 1] = temp
        current_position -= 1

print("After sort:", working_list)
