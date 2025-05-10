def linear_search(numbers, key): 
    i = 0
    while i < len(numbers):
        if numbers[i] == key:
            return i
        i += 1
    return -1

if __name__ == "__main__":
    numbers = [4, 7, 1, 9, 3, 6] 
    key = 9 
    index = linear_search(numbers, key) 
    if index != -1:
        print(f"Key {key} found at index {index}") 
    else: print(f"Key {key} not found in the list")
