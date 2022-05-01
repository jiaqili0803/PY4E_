################ex
#read through the mbox-short.txt
#figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour,

#print out the counts,
#sorted by hour as shown below.
############
file = open('mbox-short.txt')
d = dict()
for line in file:  #line是str
    if line.startswith('From '):
        line_s = line.split()   #split() splits a string into a list,line_s是list
        line_ss = line_s[5].split(':') #但line_s[5]是str，可以再split
        #print(line_ss)
        d[line_ss[0]] = d.get(line_ss[0],0) + 1
print(d)   #得出了包含时间和对应count的dict
for k,v in sorted(d.items()):  #换成tuple 排序 一个个print出来
    print(k,v)
