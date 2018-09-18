
'''
Problem:

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

'''


#solution

def domain_name(url):
    cond = 0
    domain = ''
    for value in url[::-1]:
        if value == '.':
            if cond == 1:
                break
            else:
                cond =1
                continue
        if value == '/':
            if cond ==1:
                break
        if cond == 1:
            domain = value + domain
    return domain
