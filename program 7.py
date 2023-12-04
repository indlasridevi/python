#Rearrange an array with alternate high and low elements
# Utility function to swap elements 'A[i]' and 'A[j]' in the list
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
# Function to rearrange the list such that every second element
# of the list is greater than its left and right elements
def rearrangeArray(A):
    # start from the second element and increment index
    # by 2 for each iteration of the loop
    for i in range(1, len(A), 2):
        # if the previous element is greater than the current element
        if A[i - 1] > A[i]:# swap the elements 
            swap(A, i - 1, i)
A = [9, 6, 8, 3, 2,5]
rearrangeArray(A)
print(A)