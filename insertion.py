def insertion_sort(array): 
  
    for i in range(1, len(array)): 
  
        key = array[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < array[j] : 
                array[j+1] = array[j] 
                j -= 1
        array[j+1] = key 
  
  
# Driver code to test above 
array = [2, 10, 9, 5, 6, 1, 7, 3, 8, 4] 
insertion_sort(array) 
for i in range(len(array)): 
    print ("%d" %array[i])