import random

r = random.sample(range(1000), 50)
l = [0,9,8,7,6,5,4,3,2,1]

def mergesort(lst):
    length = len(lst)
    if length == 1:
        return lst
    else:
        list1 = mergesort(lst[:length/2])
        list2 = mergesort(lst[length/2:])
    list1_length = len(list1)
    list2_length = len(list2)
    output = []
    i_l1 = 0
    i_l2 = 0
    # Case: Both lists have stuff
    while(i_l1 < list1_length and i_l2 < list2_length):
        if list1[i_l1] < list2[i_l2]:
            output.append(list1[i_l1])
            i_l1 += 1
        else:
            output.append(list2[i_l2])
            i_l2 += 1

    # Case: List1 has stuff, list2 empty
    while(i_l1 < list1_length):
        output.append(list1[i_l1])
        i_l1 += 1

    # Case: List2 has stuff, list1 empty
    while(i_l2 < list2_length):
        output.append(list2[i_l2])
        i_l2 += 1

    print(str(list1)+" + "+str(list2)+" merged into: " + str(output))
    return output

print("Case #1")
print(mergesort(l))
print("\nCase #2")
print(mergesort(r))
