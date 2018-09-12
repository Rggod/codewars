'''Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]'''




#Solution:


def list_squared(m, n):
    divisors2 = list()  # list to store the values
    divisors = list()
    for i in range(m,n):
        count = 1
        sum = 0
        while(count<= int(i**.5)):
            if (i%count) == 0:
                sum = sum + (count**2)
                if count !=(i//count):
                    sum = sum + ((i//count)**2)
            count = count +1
        a = sum**(1/2)
        if a.is_integer():
            divisors2.append([i,sum])  
        divisors.clear()
    return divisors2
    
    
 
 
# Solution2(inefficient):
# works for individual cases but not efficient for large number of sets
 
 
 def list_squared(m, n):
    divisors2 = list()  # list to store the values
    divisors = list()
    for i in range(m,n):
        count = 1
        sum = 0
        while(count<= i):
            if (i%count) == 0:
                divisors.append(count)
                sum = sum + (count**2)
            count = count +1
        a = sum**(1/2)
        if a.is_integer():
            divisors2.append([i,sum])  
        divisors.clear()
    return divisors2
