import random

random_list = []

for num in range(random.randint(5, 50)) :
    random_list.append(random.randint(1,999))

number_changed = True
upper_range = len(random_list)
while number_changed :
    number_changed = False
    for num in (range(upper_range)) :
        if num+1 < upper_range :
            if random_list[num] > random_list[num+1] :
                swap_number = random_list[num+1]
                random_list[num+1] = random_list[num]
                random_list[num] = swap_number
                number_changed = True
    upper_range -= 1

print(random_list)
