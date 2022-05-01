###print string sub and length
fruit = 'banana'
print(fruit[3])    #[3] index到string的第4位
print(len(fruit))  #len() print length of string

###loop and print each letter of a string
##way1:infinite(while)
fruit = 'banana'
index = 0   #初始index
while index < len(fruit):  #用while 循环string的长度的次数
    print(index,fruit[index])
    index = index + 1
##way2:definite(for) better！
fruit = 'banana'
for letter in fruit:   #for x in y:包括了挨个loop的意思 不需要自己定义了！
    print(letter)

###counting specific letter
word = 'banana'
count = 0  #set a count start value
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

###slice string
s = 'monty python'
print(s[0:4])  #up to 4 but not including index 4
print(s[6:20])  #[a,b]b可以超过长度 就返回到string最后一个，不会traceback
print(s[:2]) #只要头段，第0、1位
print(s[8:]) #只要尾段，第8位到结束
print(s[:])  #全部位


###string concatenate
a = 'hi'
b = a +' '+'ella'
print(b)

###in operater
if 'a' in fruit:    #直接挨个找出 输出T/F
    print('found it!')

###string comparision 只是比较首字母
#大写比小写小，Z比a小
#a<b<c<d...
#可以用 < > == 等等运算符
if 'ah' < 'ba':
    print('越开始越小')

String Library
##有很多built-in function methods，不改变原有string，只返回一个string改变过的copy
只需要 str.builtin_function() 就能调用,一些常用的：
str.capitalize() #只有首字母大写
str.find() #return你找的东西的首字母的位置（从0开始算），如果找不到就return -1
            #find("sth",位置) 从哪个位置开始找
    fruit = 'banana'
    x = fruit.find('na')
str.upper() #全变大写
str.lower() #全变小写 #often会先lower（）再find（）
"banana".lower() #或者直接在string后面加
str.replace('A','B') #replace A with B
str.strip() #delete white space
str.lstrip() #delete white space at left
str.rstrip() #delete white space at right
str.startswith('ella') #查这个str是不是以“ella”开头，返回T/F，经常和if连用 查找我们需要的那一行

###example在凌乱的信息中提取一段我想要的
data = 'ansdk asnbduqenoq@umich.edu amsdkoams'
left_side = data.find('@')
right_side = data.find(' ',left_side) #start from left_side
i_want = data[left_side+1 : right_side] #slice中间是冒号！
print(i_want)
