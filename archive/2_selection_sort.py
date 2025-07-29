"""
Select smallest element from an unsorted list in each iteration and place it at the start.
"""

def selection_sort(array):
    ###############################
    for i in range(len(array) -1):
        min_index = i
        ###############################
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        ###############################
        if array[i] != array[min_index]:
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp
   ###############################
    return array

print(selection_sort([4, 2, 6, 5, 1, 3]))


# Loop through the enire array and set min_index

# Loop though unsorted array (i+1) and if cur_index < min_index, update.

# If min_index has been updated, swap to front of unsorted list