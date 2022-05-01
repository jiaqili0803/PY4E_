#read through file with text and numbers
#extract all the numbers
#look for integers using the re.findall()
#looking for a regular expression of '[0-9]+'
#converting the extracted strings to integers
#summing up the integers

'''Sample data: regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: regex_sum_1311326.txt (There are 100 values and the sum ends with 923)'''


######################
#sample data
import re

file = open('regex_sum_1311326.txt')
l = list()
for line in file:  #line is list
    line = line.rstrip()
    nums_each_line = re.findall('[0-9]+',line)  #list of strings of intgers
    #print(nums_each_line)
    for i in nums_each_line:
        if i != None:
            l.append(i)  #l contains all integers in a list of string
#print(l)

l_int = list()
for i in range(len(l)):
    l_int.append(int(l[i]))
print(l_int)
print('length: ', len(l_int))
print('sum: ', sum(l_int))

