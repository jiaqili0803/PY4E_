###open（） open的是objective,相当于给了你一个操纵file的工具
fname = open('xx.txt',r) #returns a file object which can used to read, r可以省略
fname = open('xx.txt',w) #write

###换行符
\n #放在string里面 实际占一个字符length

###read（）
a = xfile.read() # read the whole file into a variable as a single string

###for loop,maybe if加进去
xfile = open('xx.txt',r)
for x in xfile:  #file里面一行 为一个sequence，一行一行print出来
    print(x)

###寻找以xxx开头的行们
#for loop with if for specific star"From"
xfile = open('xx.txt',r)
for line in xfile:
    line = line.rstrip()  #去掉文本右边的\n，不然加上print（）带的就会有空白行
    if line.startwith("From:"):
        print(line)
#上面的if not, continue写法
xfile = open('xx.txt',r)
for line in xfile:
    line = line.rstrip()
    if not line.startwith("From:"): #if not
        continue
    print(line)

###寻找有umich的行们
for line in xfile:
    line = line.rstrip()
    if not "umich" in line:
        continue   #如果没有就skip
    print(line)

###prompt for file name,找这个file有多少subject line
fname = input('plz enter the filename: ')
try:  #catch error
    xfile = open(fname)  #return a file object
except:
    print("file can not be read:",fanme)
    quit()  #不执行之后的

count = 0  #set start
for line in xfile:
    if line.startwith("Subject"):
        count = count + 1
print("there are ",count,"subject lines in",fname)
