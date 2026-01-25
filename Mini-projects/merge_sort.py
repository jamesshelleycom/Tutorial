import random

random_list = []

for num in range(random.randint(5, 15)) :
    random_list.append(random.randint(1,999))

print("UNSORTED list:", random_list)

def merge_sort(input_list) :
    new_list = []
    not_finished = True
    if len(input_list) <= 1 :
        return input_list
    else :
        sublist_1 = input_list[:len(input_list)//2]
        sublist_1 = merge_sort(sublist_1)
        sublist_2 = input_list[len(input_list)//2:]
        sublist_2 = merge_sort(sublist_2)

        while not_finished :

            if sublist_1 and sublist_2:
                if sublist_1[0] < sublist_2[0] :
                    new_list.append(sublist_1.pop(0))
                else :
                    new_list.append(sublist_2.pop(0))
            elif sublist_1 and not sublist_2:
                new_list += sublist_1
                not_finished = False
            elif not sublist_1 and sublist_2 :
                new_list += sublist_2
                not_finished = False
            else :
                not_finished = False
    return new_list

print("SORTED list:", merge_sort(random_list))
