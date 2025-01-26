# Chapter #2 - Selection Sort

# example array = [4, 2, 6, 1, 7]

# Program for finding the smallest element in an array

def find_smallest(list): 
    smallest = list[0]
    smallest_index = 0
    
    for i in range(len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
            
    return smallest_index

# Selection Sort program

def selection_sort(arr): 
    new_list = []
    copy_list = list(arr)
    
    for i in range(len(copy_list)):
        smallest = find_smallest(copy_list)
        new_list.append(copy_list.pop(smallest))
    
    return new_list

print(selection_sort([4, 2, 6, 1, 7]))