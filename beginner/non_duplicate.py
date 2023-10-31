def non_duplicate(original_array):
    """Funtion that eliminates the duplicated values on a list

    Args:
        original_array (array []): Receive an array

    Returns:
        array[]: returns the array with no duplicated valued
    """
    original_array.reverse()
    for element in original_array:
        counter = original_array.count(element)
        while counter > 1:
            original_array.remove(element)
            counter = original_array.count(element)
    original_array.reverse()
    return original_array.reverse()


non_duplicate([1, 2, 3, 1, 2, 4, 5, 6, 10, 10])
