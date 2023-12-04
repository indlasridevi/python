def sort_by_frequency(arr):
    # Create a dictionary to store the frequency of each element
    frequency_dict = {}
    for element in arr:
        # Update the frequency count in the dictionary
        frequency_dict[element] = frequency_dict .get(element, 0) + 1
    # Sort the array based on frequency and then by the element it
    sorted_arr = sorted(arr, key=lambda x: (frequency_dict[x], x))
    return sorted_arr
# Input the number of test cases
t = int(input())
for _ in range(t):
    # Input the size of the array
    n = int(input())
    elements = list(map(int, input().split()))
    # Call the function to sort the array by frequency
    sorted_result = sort_by_frequency(elements)
    print(sorted_result)