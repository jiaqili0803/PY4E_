import re

x = 'my 2 give 30 a 444, them 666'

y = re.findall('[a-z0-9]',x)  
print(y)     
