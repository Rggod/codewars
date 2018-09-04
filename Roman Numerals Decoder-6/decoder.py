def solution(roman):
  """complete the solution by transforming the roman numeral into an integer"""
  values = {'I' : 1 ,'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
  sum  = 0
  count = 0
  while(count < len(roman)):    
      cur = values.get(roman[count],' ')
      if count == len(roman) -1  or (cur >= values.get(roman[count+1],' ')):
          sum = sum + cur
      else:
          sum = sum +(values.get(roman[count+1],' ')-cur)
          count = count +1
          
      count = count +1
          
  return sum
