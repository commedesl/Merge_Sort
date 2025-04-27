def merge_sort(array):
    # Base case: If the array has 0 or 1 element, it's already sorted
    if len(array) <= 1:
        return

    # Step 1: Divide - Split the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point] 
    right_part = array[middle_point:]

    # Step 2: Recursively sort both halves
    merge_sort(left_part)    # Recursive call on left half
    merge_sort(right_part)   # Recursive call on right half

    # Step 3: Merge - Combine sorted halves into original array
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Compare elements from left and right arrays, and copy the smaller one
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else: 
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copy remaining elements from left_part, if any
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # Copy remaining elements from right_part, if any
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

# Test the merge_sort function
array = [4, 10, 6, 14, 2, 1, 8, 5]
merge_sort(array)
print(array)  # Output: [1, 2, 4, 5, 6, 8, 10, 14]
