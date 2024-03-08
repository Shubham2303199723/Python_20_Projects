# Binary Search algoritham is a searching allgoritham to match value in list with given by user 
# a function will take an list and target parameter
# multiple variables : middle, start, end, steps
# recursion and while loop
# increase the steps each time a split is done 
# condition to track the target 
# binary search divide list of elemrnt by 2 for finding middle number in list


def binary_search(list, element):       # for search any element we have to give list without it it will not work and give target by user
    middle = 0
    start = 0
    end = len(list)                     # this is end number of list element where len method will return length of list for loop
    steps = 1                           # to count steps in how many steps it searched user target 
    while(start<=end):
        print("Steps", steps, ":", list[start:end+1])  # you can convert list in string if any error occurs
        steps = steps + 1
        middle = (start + end) // 2     # this method use for getting point of middle point in list 
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1 
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 12
binary_search(my_list, target)