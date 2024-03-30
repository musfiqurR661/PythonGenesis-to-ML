def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_count = count_inversions(arr[:mid])
    right_half, right_count = count_inversions(arr[mid:])
    merged_arr, merge_count = merge_with_count(left_half, right_half)

    return merged_arr, left_count + right_count + merge_count


def merge_with_count(left, right):
    result = []
    count = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i

    result.extend(left[i:])
    result.extend(right[j:])
    return result, count


# Example usage:
arr = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
sorted_arr, inversions = count_inversions(arr)
print("Sorted Array:", sorted_arr)
print("Number of Inversions:", inversions)
