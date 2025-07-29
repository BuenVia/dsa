"""
Place an unsorted element at its suitable place in each iteration.
Like sorting cards - assume first card is sorted, select next unsorted and place to right if greater, else place to left.
"""

def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i-1
        while temp < array[j] and j > -1:
            array[j+1] = array[j]
            array[j] = temp
            j -= 1
    return array

print(insertion_sort([4, 2, 6, 5, 1, 3]))

# Loop through the array but starting at the second item in the list
# Assign cur_index to temp variable
# Assign cur_index-1 to another variable
# While loop that compares the cur_index and and cur_index-1 and if cur_index is less then swap values of cur_index and cur_index-1 until cur_index-1 is less than cur_index.
# Replace cur_index-1 with a further -1
# Include condition to avoid the lowest number going back further than the index of 0.
