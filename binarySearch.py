# This implementation of binary search has a time complexity of O(log n), which makes it very efficient for large lists. It works by dividing the list in half repeatedly until the item is found, or it is clear that the item is not in the list

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Example usage
my_list = [1, 3, 5, 7, 9, -1, 4, 5, 6, 1, 3, 8, 10]
print(binary_search(my_list, 4)) # Output: 1
print(binary_search(my_list, 8)) # Output: None
