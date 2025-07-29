# Fibonacci Sequence
def fibonacci(n: int):
    prev2 = 0
    prev1 = 1

    print(prev2)
    print(prev1)

    for _ in range(n):
        new_fibo = prev2 + prev1
        print(new_fibo)
        prev2 = prev1
        prev1 = new_fibo

# fibonacci(18)

# Arrays
# Find the lowest value in an array
"""
1. Create a variable 'min_value' and set it equal to the first value of the array
2. Go through every element in the array
3. If the current element has a lower value than 'min_value', update 'min_value' to be this value
4. After looking at all of the elements in the array, the 'min_value' now contains the lowest value
"""
def find_lowest():
    my_array = [99, 34, 74, 33, 50, 53, 97, 3, 69, 22]

    min_value = my_array[0]
    for i in my_array:
        if i < min_value:
            min_value = i
    print(f"Lowest value is: {min_value}")

# find_lowest()

# Bubble Sort
def bubble_sort():
    my_array = [64, 34, 25, 12, 22, 11, 90, 5]

    n = len(my_array)
    for i in range(n-1):
        for j in range(n-i-1):
            x = [my_array[j], my_array[j+1]]
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    print(f"Sorted array: {my_array}")

bubble_sort()

def bubble_sort_two():
    my_array = [64, 34, 25, 12, 22, 11, 90, 5]
    for i in range(len(my_array) -1, 0, -1):
        for j in range(i):
            if my_array[j] > my_array[j+1]:
                temp = my_array[j]
                my_array[j] = my_array[j+1]
                my_array[j+1] = temp
    print(my_array)

# bubble_sort_two()

def selection_sort():
    my_array = [64, 34, 25, 5, 22, 11, 90, 12]
    
    n = len(my_array)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        min_value = my_array.pop(min_index)
        my_array.insert(i, min_value)
    print("Sorted Array: ", my_array)


# selection_sort()