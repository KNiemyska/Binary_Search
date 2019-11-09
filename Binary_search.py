#FIRST SORT ARRAY - BUBBLE SORT
def swapPositions(list,pos1,pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def bubble_sort(array):
    counter=-1
    length = len(array)
    while counter!=0:
        counter=0
        for i in range(0,length-1):
            if array[i]>array[i+1]:
                swapPositions(array,i,i+1)
            counter+=1
        length-=1
    return array

#BINARY SEARCH

def binary_search(array,start_point,end_point,target):

    if start_point<=end_point:
        middle_point =int((start_point+end_point)/2)
        if array[middle_point]==target:
            return middle_point
        elif target<array[middle_point]:
            return binary_search(array,start_point,middle_point-1,target)
        else:
            return binary_search(array,middle_point+1,end_point, target)
    else:
        return -1

# Function call
#MAIN
input_array=[25,17,15,1,9,19,34,8,7,20,13,11]
target=19
arr=bubble_sort(input_array)

result = binary_search(arr, 0, len(arr) - 1, target)


if result != -1:
    print(f"Element is present at index {result}")
else:
    print( "Element is not present in array")



