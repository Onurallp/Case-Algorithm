def find_winter_summer(arr):
    if not arr:
        raise ValueError("Array is empty. Cannot partition.")

    low_numbers = [arr[0]]  # Initialize the low_numbers array with the first element
    high_numbers = []

    for num in arr[1:]:  # Check elements starting from second index.
        # Check prior element and check if all elements in high_numbers are indeed bigger than each element of low_numbers array
        if num >= low_numbers[-1] and all(num > x for x in low_numbers):
            high_numbers.append(num)
        else:
            # check if elements in low_numbers are indeed smaller than each element of the high_numbers array
            if all(num < x for x in high_numbers):
                low_numbers.append(num)
            else:
                high_numbers.append(num)

    return low_numbers, high_numbers
