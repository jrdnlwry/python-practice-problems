import random

def listOverLap(list1, list2):
    """
    This function accepts two parameters
    list1: randomized list object containing INTs
    list2: randomized list object containing INTs
    """

    common_list = []
    # for each element in the list if there's a match add it to the new list
    for elem in list1:
        if elem in list2:
            common_list.append(elem)
    return common_list

# call the function w/ two randomized list from within the specified range
# print the output
print(listOverLap(random.sample(range(0, 100), 25), random.sample(range(0, 100), 25)))
