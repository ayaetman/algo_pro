def insertion_sort(array):  
    for i in range(1, len(array)): 
       key = array[i] 
       j = i-1
    while j >=0 and key < array[j] : 
       array[j+1] = array[j] 
       j -= 1
       array[j+1] = key 
    
#test
array = [2, 10, 9, 5, 6, 1, 7, 3, 8, 4] 
insertion_sort(array) 
for i in range(len(array)): 
    print ("%d" %array[i])
