
###greedy matching (*and+) 默认取最大范围的string下来
import re
x = 'From: Using the : chat'
y = re.findall('^F.+:',x)
print(y)
>>['From: Using the :']  #取范围大的

###non-greedy matching (?)
import re
x = 'From: Using the : chat'
y = re.findall('^F.+?:',x)   #多加了一个？就不贪心了
print(y)
>>['From:']

###fine-tune by ()括号
x= 'From zqian@umich.edu Fri Jan  4 16:10:39 2008'
y = re.findall('^From (\S+@\S+)', x)   #里面这个括号指定了具体extract什么
print(y)
>>['zqian@umich.edu']

###[^ABC] #[^ ]：match non-blank character
import re
x= 'From zqian@umich.edu Fri Jan  4 16:10:39 2008'
y = re.findall('@([^ ]*)',x) # @:look through until find this sign;
print(y)                     # *: match多个characters，不然只match@后的一个u
>>['umich.edu']
y = re.findall('^From .*@([^ ]*)',x)  #.*: any 0 or more than 0的 characters
print(y)
>>['umich.edu']

###提取文章中某些行的数字部分 并找到最大值
#X-DSPAM-Confidence: 0.8475 样例行
import re
file = open('mbox-short.txt')
l = list()
for line in file:
    line = line.rstrip()    #line is a list here
    #print(line)
    x = re.findall('^X-DSPAM-Confidence: ([0-9.]*)',line)  #.代表有float;这里返回list of str;抓不到的行返回的是[]
    if len(x) != 1:  #明确只要每行的那1个digit
        continue
    #print(x)
    l.append(float(x[0]))  #得到一个只有所需数字的list; float只能对str不能对list
print(l)
print('max value: ',max(l))

###反斜线 backslash'\' prefix the sign you want(这些sign已有syntax)
x = 'we got $10.00 for you'  #we want real "$"sign but not its syntax: use "\"
y = re.findall('\$[0-9.]*',x) #\$:real $ sign
print(y)
>>['$10.00']
