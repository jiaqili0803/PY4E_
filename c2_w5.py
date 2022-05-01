#常规variable不是collection，赋值后会被覆盖
#list, dictionary是collection,一个variable可以包含多个内容

###list, dictionary区别
#list:collection stay in order
#dictionary: a 'bag' of values, each with its own label，no order
#list用num(从0开始)查value，dict用key查value

###what is dictionary
p = dict() #set a new dictionary
p['money'] = 12 #每个value都有一个key；value(12)有一个key(money)
p['candy'] = 3  #通过key键入他的value
p['tissue'] = 75
print(p)
>>{'money':12,'tissue':75,'candy':3}  #key-value pairs 组成dictionary
                                      #dict的内部顺序不固定
p['candy'] #通过key调出他的value
>>3

#mutable
p['candy'] = p['candy'] + 2 #根据key更改其value值
p['candy'] = 5 #或者这样
print(p)
>>{'money':12,'tissue':75,'candy':5}

#setup a dict
x = {'money':12,'tissue':75,'candy':5}  #赋值建立一个字典 不一定是string-num形式
o = {}  #建立一个空字典

#in operator 查询是否存在在dict里面
#如果尝试print dict里面没有的key，会error
'apple' in x
>>>False

###用字典 数名字出现的次数
names = ['ella','ella','alice','bo','alice']
counts = dict() #set new dictionary
for name in names:
    if name not in counts:  #没有就新建一个key
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1 #有就key对应的value加1
print(counts)
>>{'ella':2,'alice':2,'bo':1}

###用字典 数名字出现的次数--easier way use .get()
names = ['ella','ella','alice','bo','alice']
counts = dict()
for name in names:
    counts[name] = counts.get(name,0) + 1 #代替上面if else loop包含的逻辑
print(counts)

###数一段话中每个词出现的次数
counts = dict()
passage = input('plz enter a passage: ')
words = passage.split()  #split passage into words
for word in words: #loop每一个word
    counts[word] = counts.get(word,0) + 1  #相当于现值+1(新count的一次，新值)
print(counts)

###for loop写出key和key对应的value
counts = {'ella':2,'alice':2,'bo':1}
for key in counts:  #loop的是 all the key
    print(key, counts[key])


###built-in funtion methods
#以counts这个dict举例来写
dict.get() ##查key对应的value，以及这个key存在不
        x = counts.get(name, 0) #在dict counts中查name这个key对应的value并返回
                                #0意思if the specified key does not exist， 默认返回0不error
list(counts) #把所有key转化为一个list
counts.keys() #get list of keys from a dict
counts.values() #get list of values from a dict, 和keys()的list一一对应
counts.items() #get list of pairs of key-values in tuple format
        >>>[('ella',2),('alice',2),('bo',1)]

###two interation variables
counts = {'ella':2,'alice':2,'bo':1}
for aaa,bbb in counts.items(): #两个值同时loop，一个loop key，一个loop value
    print(aaa,bbb)

###找一个文章中出现次数最多的词和次数
file_name = input("you want to find this passage: ")
file = open(file_name)
#words = file.split()  #objective不能直接split，只有list可以

counts = dict()
for line in file:   #只能这么读objective
    line_s = line.split() #line是objtect的一行，可以split成list
    for word in line_s:  #每一行去loop 直到全部loop完做成dict
        counts[word] = counts.get(word,0) + 1
print(counts)

bigword = None  #set初始的 最大word及其次数
bigcount = None
for word,count in counts.items():   #loop他的key-value
    if bigcount is None or bigcount < count:  #if...is...or...
        bigcount = count
        bigword = word
print("biggest word and count: ",bigword,bigcount)
