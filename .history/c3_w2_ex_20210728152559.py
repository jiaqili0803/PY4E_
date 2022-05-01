#read through file with text and numbers
#extract all the numbers
#look for integers using the re.findall()
#looking for a regular expression of '[0-9]+'
#converting the extracted strings to integers
#summing up the integers

Sample data: regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: regex_sum_1311326.txt (There are 100 values and the sum ends with 923)


######################
#sample data
import re

file = open('regex_sum_42.txt')
l = list()
for line in file:  #line is list
    line = line.rstrip()
    nums_each_line = re.findall('[0-9]*',line)  #list of strings of intgers
    l.append(nums_each_line)  #l contains all list of strings of nums we want
#l_int = int(l)  
#convert to integers; int()can only convert strings but not list!!!
print(l)
'''
l_int = list()
for i in l:
    l_int = l_int.append(int(l[i]))
print(len(l_int))
print(sum(l_int))

l_int = list()
l = ['2','5','78']
for i in l:
    l_int = l_int.append(int(l[i]))
print(l_int)
