def mergeSort(arr):
    """
    Time Complexity:
        Worst complexity: n*log(n)
        Average complexity: n*log(n)
        Best complexity: n*log(n)
    Space complexity: n
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_array = arr[:mid]  # Dividing the array elements
        right_array = arr[mid:]  # into 2 halves

        mergeSort(left_array)  # Sorting the first half
        mergeSort(right_array)  # Sorting the second half

        left_arr_index = right_arr_index = merge_arr_index = 0

        # Copy data to temp arrays L[] and R[]
        while left_arr_index < len(left_array) and right_arr_index < len(right_array):
            if left_array[left_arr_index] < right_array[right_arr_index]:
                arr[merge_arr_index] = left_array[left_arr_index]
                left_arr_index += 1
            else:
                arr[merge_arr_index] = right_array[right_arr_index]
                right_arr_index += 1
            merge_arr_index += 1

        # Checking if any element was left
        while left_arr_index < len(left_array):
            arr[merge_arr_index] = left_array[left_arr_index]
            left_arr_index += 1
            merge_arr_index += 1

        while right_arr_index < len(right_array):
            arr[merge_arr_index] = right_array[right_arr_index]
            right_arr_index += 1
            merge_arr_index += 1
