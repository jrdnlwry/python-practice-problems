def linearSearch(arg, numArray):
    """
    Simple linear search algorithm that accepts two inputs and returns the position of a given value in the array.

    arg -> int
    numArray -> list object
    """
    # check to see if the input parameter is an integer value
    if not isinstance(arg, int):
        print("not an integer value")
        return

    for index, value in enumerate(numArray):
        if arg == value:
            print(f"The number {arg} is at index {index}")
            return

    print(f"{arg} is not in the array.")

linearSearch(34, [1, 5, 7, 8, 10, 25, 2])
