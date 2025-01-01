def sum_two_smallest_numbers(numbers):

    """
    Sorts a list of integers in ascending order using a selection sort algorithm.

    This function iterates through the given list, finding the smallest element in each iteration and appending it to a new list, effectively sorting the elements. The original list is modified during the process as the smallest elements are removed in each iteration.

    Parameters:
    num (list of int): A list of integers that needs to be sorted.

    Returns:
    list of int: A new list containing the sorted integers from the input list.

    """

    # A list to hold the sorted integers
    sortedNum = []
    
    # Continue sorting until the original list is empty
    while len(numbers) > 0:
        # Assume the first element is the smallest initially
        min_index = 0

        # Iterate through the list to find the smallest element
        for i in range(1, len(numbers)):
            # Update the index of the smallest element if a smaller element is found
            if numbers[i] < numbers[min_index]:
                min_index = i

        # Append the smallest element to the sorted list
        sortedNum.append(numbers[min_index])
        # Remove the smallest element from the original list
        numbers.pop(min_index)
    
    sortedN = (sortedNum[0], sortedNum[1])
    
    
    return sortedN[0] + sortedN[1]