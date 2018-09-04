'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:
'''


def find_uniq(arr):
    # your code here
    count = 0
    while arr[count] == arr[count+1]:
        count = count + 1
    if count == 0:
        if arr[count + 1] == arr[count +2]:
            return arr[count]
        else:
            return arr[count+1]
    return arr[count+1]   # n: unique integer in the array
