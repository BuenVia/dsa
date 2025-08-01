"""
Compare two adjacent elements and swap them until they are in order.
"""

def bubble_sort(array):
    for i in range(len(array) -1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array

print(bubble_sort([4,2,6,5,1,3]))