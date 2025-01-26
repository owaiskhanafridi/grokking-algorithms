
# Binary Search

#Example List => [1, 3, 5, 7, 8, 50, 59, 70, 80, 99], Find 3
# Big(O)==> log2 n = log2 10 = 3

def binary_search(list, element):
    start=0
    end=len(list)-1
    iteration_count=0
    while start <= end:
        iteration_count = iteration_count + 1
        mid = (start + end) // 2
        if element == list[mid]:
            print(f'element equal to the middle position. Iteration: {iteration_count}')
            return mid
        elif element < list[mid]:
            end = mid - 1
            print(f'element less than the middle position. Iteration: {iteration_count}')
        else: 
            start = mid + 1
            print(f'element greater than the middle position. Iteration: {iteration_count}')
    return None    

print(binary_search([1, 3, 5, 7, 8, 50, 59, 70, 80, 99], 80))

