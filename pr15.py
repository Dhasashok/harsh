def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not found

# Example usage
arr = [5, 3, 7, 9, 2]
target = 7
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")

