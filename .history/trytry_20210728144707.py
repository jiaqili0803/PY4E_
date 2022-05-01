import re
x = 'my 2 give 30 a 444, them 666'

y = re.findall('[0-9]+',x)  #find and exract all digits
print(y)     