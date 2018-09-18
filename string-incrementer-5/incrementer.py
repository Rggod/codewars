'''
Problem:

Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

'''

# solution


def increment_string(strng):
    num = ('1','2','3','4','5','6','7','8','9','0')   # list of numbers
    num1 = ''
    output = ''
    cond  = 0   # change this to 1 once a letter is detected 
    for value in strng[::-1]:  # read in reversible order to find the number values first
        if value not in num:
            output = value + output
            cond = 1
        elif cond == 1:
            output = value + output
        else:
            num1 = value + num1
    size =  len(num1)
    if len(num1) ==0:   # checks if there is no number present
        num1 = 1
    else:
        num1 = int(num1)+1
    output = output+(str(num1).zfill(size))
    return output
