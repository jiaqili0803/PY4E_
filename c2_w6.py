'''
### sorted(list) and list.sort() difference
Use list.sort() when you want to mutate the list
use sorted() when you want a new sorted object back, dont affect the original list
Use sorted() when you want to sort something that is an iterable, not a list yet.


Tuples are like Lists 只不过变成圆括号
都是index从0开始的sequence

x = ('a','b','c')
print(x[2]) #index

y = (1,2,3) #constant赋值
print(y)
>>(1,2,3)

max(y) #max()
>>3

for s in y:  #for loop
    print(s)

但是，tuples are immutable，similar to string
所以：
x.sort()
x.append()
x.reverse()
x.extend()
....都不行！！都会error

tuple与list在可用函数method上的区别：
l = list()
dir(l)
>>>[ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
t = tuple()
dir(t)
>>>['count', 'index']

tuple比list更高效，不占内存，
如果要弄 临时用一下的variable就丢弃 以后也不会再用/改动的 可以选tuple

###tuple assignment赋值 可以放左边
(x,y) = (4,'hi')  #左右对应 都是tuple

###items() in dictionary,returns a list of (key,value) Tuples
d = dict()
d['a'] = 2
d['b'] = 4
for k,v in d.items():
    print(k,v)

tups = d.items()
print(tups)
>>dict_items([('a', 2), ('b', 4)])

###tuples comparable #从左开始，一对一对儿看，只要一对儿对了就是对了
(0,1,2) < (5,1,2)  #0<5，对了， 后面的都不看了
>>True
(0,1,2000) < (0,3,4) #0=0，1<3,对了
>>True
('jone','sally') < ('jone','sam') #jone一样，sa一样，l<m 对了
>>True

### sort dict by tuples 可以用这个优点来排序dict
##按key排序
d = {"c":22,'b':1,'a':10}  #dict
t = sorted(d.items)  #基于tuples排序原则 按key排序
t
>>[('a',10),('b',1),("c",22)]

for k,v in sorted(d.items):
    print(k,v)     #>>得到按key排序后的sequence
>> a 10
>> b 1
>> c 22

##按value排序
c = {"c":22,'b':1,'a':10}
tmp = list()
for k,v in c.items():
    tmp.append((v,k)) #append() 每对tuple(v,k) 双重括号
tmp_sorted = sorted(tmp,reverse = True) #从高到低
print(tmp_sorted)
>>[(22, 'c'), (10, 'a'), (1, 'b')]


########找top 10 most common words
#把文章的所有不重复word及其count写进dict
file = open('romeo.txt')
d = dict()
for line in file:
    line_s = line.split()
    for word in line_s:
        d[word] = d.get(word,0) + 1
print(d)
#把dict按value排序
l = list()
most_10 =list()
for k,v in d.items():
    l.append((v,k))  #list.append()不返回新list 直接修改原有list，不要赋值给左边
l_ordered = sorted(l,reverse = True)
print(l_ordered)
#取value高的前10个-按k,v print出来
for v,k in l_ordered[:10]:
    print(k,v)

#把dict按value排序-----方法二 list comprehension
sorted([(v,k) for (k,v) in d.items() ],reverse = True)
