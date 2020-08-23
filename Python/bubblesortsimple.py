#!/bin/python3.8

# Python program for sorting entered numbers

# n is variable for array length (number of sorted elements) 
n=int(input("Please enter number of sorted elements: "))
array=list(map(int,input("Enter the elements, split them using space:").strip().split()))[:n]

# Traverse through all array elements
for i in range(n-1):
 # range(n) also work but outer loop will repeat one time more than needed.

    for j in range(0, n-i-1):
        # traverse the array from 0 to (n-i-1), we could use (n-1) also but, we will check also sorted part what is unnecessary 
        # Swap if the element found is greater
        # than the next element
        if array[j] > array[j+1] :
          array[j], array[j+1] = array[j+1], array[j]

# print sorted array
print ("Sorted elements are:", array)
