###计数
counter = 0 #set start value
for num in [9,41,12,3,74,15]:
    counter = counter + 1 #iterate一次就计数一次
    print(counter,num)

###求和
total = 0  #set start value
print('Before:',total)
for num in [9,41,12,3,74,15]:
    total = total + num  #加和
print('After:',total)

###平均数
count = 0  #set start value
sum = 0
print('Before:',count,sum)
for num in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + num
    print(count,sum,num)  #可以看到过程
print('After:the average is',sum/count)

###filter
for num in [9,41,12,3,74,15]:
    if num > 20:    #if来引导过滤
        print('Large num: ',num)

###Boolean #只返回T/F
#False/True 是constant不是variable
###寻找是否有某个值
found = False  #初始为false 找到了变True
for num in [9,41,12,3,74,15]:
    if num == 3:
        found = True
        break  #一旦找到就不再循环后面无用的直接跳出
print("There is a 3:",found)

###find the min value
min_so_far = None    #不用具体数字，用None set初始flag value更合理
for num in [9,41,12,3,74,15]:
    if min_so_far is None:  #if...is比==更强：exactly完全相等
        min_so_far = num    #如果初始值为none 就赋值为第一个num
    elif num < min_so_far:  #elif继续比较
        min_so_far = num
print("The min is: ",min_so_far)

###求用户输入的值们的sum/num/average
num = 0
sum = 0
while True: #可能是infinite次，所以用while引导的True
    number = input("plz enter the number: ")
    if number == "done":   #避免无限进行下去
        print("Done!!!")
        break
    try:
        number_f = float(number) #危险语句 如果用户输入非numeric
    except:
        print("invalid input!")
        continue   #跳回上面进行下一次loop
    sum = sum + number_f
    num = num + 1
print("Sum is： ",sum," Num is: ",num," Average is: ",sum/num)

###求用户输入的值们的largest smallest
min = None
max = None

while True: #可能是infinite次user input，所以用while引导的True
    number = input("plz enter the number: ")
    if number == "done":  #给机会出来
        print("Done!!!")
        break
    try:      #catch error
        number_f = int(number)
    except:
        print("Invalid input")
        continue

    if min is None: #找min
        min = number_f
    elif min > number_f:
        min = number_f

    if max is None:  #找max
        max =number_f
    elif max < number_f:
        max = number_f

print('Minimum is',min)
print('Maximum is',max)
