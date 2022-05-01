#可以包含什么
[1,[5,6],7] #是3 element list, list可以包含list
['red',23,5.7] #可以包含不同类型
[] #可以创建空list
x = list()

#index operator中括号定位
friends = ['ella','lee','alice']
print(friends[1])  #>>lee

#list are mutable可改变, 改变原有element
loto = [1,2,3,4,5]
loto[2] = 7  #替换成功！
        #而string不可以!!，immutable，可以用函数make and change new string
        fruit = 'Banana'
        fruit[0] = 'b' #will error
        x = fruit.lower() #可以这样

###list methods functions，一些会改变原有list！！
#可以写成function(x) or x.function()
len()  #length of elements, can be different types
max()
min()
sum()
range() #return a sequence of numbers from 0, up to but not include the last
        range(4)  #>>range(0, 4)
        list(range(4))     #>>[0,1,2,3]
        friends = ['ella','lee','alice']
        list(range(len(friends))) #>>[0,1,2]
append()  #append an element at the end of list
        x = list() #set a empty list
        x.append('book')
        x.append(99)
count()
extand()
sort() #sort in alphabet order, num从小到大
split() #split the srting to a list contains all elements
        #默认以空格（or多个空格）拆分
        #也可以自定义用什么拆分
        #可以重复split直到找到想要的
        line = 'hi;hello;you'
        line_splited = line.split(';') #以“；”拆分
        >> ['hi','hello','you']
        #可以用来找 相同位置的东西 代替 find() 会easier
...

###counted loop 不用i去遍历实际内容而是遍历他的index
#这样可以知道i对应的值，比for friend in friends:更好用
friends = ['ella','lee','alice']
for i in range(len(friends)):   #range(len())创造i要遍历的数字范围
    friend = firends[i]  #可以定位
    print("happy new year: ",friend)


###concate
a = [1,2,3]
b = [4,5,6]
c = a + b  #just +
c = [1,2,3,4,5,6]

###slice list 注意前闭后开
c = [1,2,3,4,5,6]
c[1:3] #从0开始 第1位到不包括第3位 >>[2,3]
c[:4] #开头到不包括第4位 >> [1,2,3,4]
c[3:] #第3位到结束 >>[4,5,6]
c[:] #全部

###in and not in operater 直接返回T/F
c = [1,2,3,4,5,6]
3 in c #>>True
9 in c #>>False
30 not in  c #>>True

###用list的funtion来写loop 与之前的传统loop比较
#优缺：more eaiser，especially already have a list;but waste more memory
##1. 传统求average 手动定义loop
total = 0
count = 0
while True:
    inp = input('enter the num: ')
    if inp == "done":
        break
    value = float(inp)
    total = total + value
    count = count + 1
print("average:",total/count)

##2. list来写loop
newlist = list() #set new list
while True:
    inp = input('enter the num: ')
    if inp == "done":
        break
    value = float(inp)
    newlist.append(value)  #直接每次都存进去
print("average:",sum(newlist)/len(newlist)) #直接用sum() len()
