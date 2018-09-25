'''
 Problem:
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]



NOTE The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2 The 0x0 (empty matrix) is represented as [[]] '''

# solution

def snail(array):
    if len(array) ==1:
        for value in array:
            return value
    ordered = list()
    while len(array)>0:
        ordered.extend(array[0])
        del array[0]
        for x in array:
            ordered.append(x[-1])
            del[x[-1]]
        if len(array)>0:
            ordered.extend(array[-1][::-1])
            del[array[-1]]
        for x in array[::-1]:
            ordered.append(x[0])
            del[x[0]]
    return ordered
