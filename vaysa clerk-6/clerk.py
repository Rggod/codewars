'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

Examples:

tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
'''

def tickets(people):
    bill25 = 0    # count of the 25 dollar bills
    bill50 = 0    # count of the 50 dollar bills
    mprice = 25   # price of ticker
    for value in people:
        if value == 25:
            bill25 = bill25 + 1
        if value == 50:
            bill50 = bill50 + 1
            
        if value > 25:
            change = value - mprice
            if change == 25:    
                if bill25 > 0:
                    bill25 = bill25 - 1
                else:
                    return "NO"
            if change  == 75:
                if (bill25 >0 and bill50 >0):
                    bill25 = bill25 - 1
                    bill50 = bill50 - 1
                elif bill25 > 2:
                    bill25 = bill25 -3
                else:
                    return "NO"
                    
    return "YES"
    return "?"
