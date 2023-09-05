# Remove duplicates from sorted array
# Example 1: input array is [1,1,2,2], the function should return 2.
# Example 2: input array is [1,1,2,3,3], the function should return 3.

def removeDuplicates(array):
    size = len(array)
    insertIndex = 1
    for i in range(1, size):
        if array[i - 1] != array[i]:
            # Updating insertIndex in our main array
            array[insertIndex] = array[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex

array_1 = [1,2,2,3,3,4]
print(removeDuplicates(array_1))