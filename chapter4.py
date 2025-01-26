#Chapter 4 - QuickSort


#Recursive function to calculate sum of array using Divide & Conquer Rule

#Excercise 4.1: Write out the code for the earlier sum function
def sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])
    
print(sum([2,4,6]))

#Exercise 4.2: Write a recursive function to count the number of items in a list
def count(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 1
    else:
        return 1 + count(arr[1:])

print(count([2,4,6]))

#Exercise 4.3: Write a recursive function to find the maximum number in a list

def find_max(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        current_max = arr[0]
        new_max = find_max(arr[1:]) 
        if current_max <= new_max:
            return new_max
        else:
            return current_max
print(find_max([2,4,33,6, 1]))
            

#LearntOnTheWay
# For Comparison, max_value: float('inf'), min_value = float('-inf')

#Exercise 4.4: Remember binary search from chapter 1? It’s a D&C algorithm, too. 
# Can you come up with the base case and recursive case for binary search?

def binary_search(arr, element, start=0, end=None):
    if end is None:  # Initialize `end` on the first call
        end = len(arr) - 1

    # Base case: Element not found
    if start > end:
        return None

    mid = (start + end) // 2

    if element == arr[mid]:
        return mid
    elif element < arr[mid]:
        # Search in the left half
        return binary_search(arr, element, start, mid - 1)
    else:
        # Search in the right half
        return binary_search(arr, element, mid + 1, end)

# Test the function
print(f'binary search result: {binary_search([1, 3, 5, 7, 8], 3)}')


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        
        return quicksort(lesser) + [pivot] + quicksort(greater)