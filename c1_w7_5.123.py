###indefinite loop
#break
while True:  #True会一直T一直循环
    line = input("try input something>>")
    if line == 'done':
        break   #加if引导的break来触发 跳出loop
    print(line)
print("Done!!")  #直接跳到while loop之外

#continue
while True:
    line = input("try input something>>")
    if line[0] == "#":  #加if引导的continue来触发，直接跳回loop开头
        continue
    if line == 'done':
        break
    print(line)
print("Done!!")

###definite loop
for i in [5,4,3,2,1]: #一般用i来做numberic iterate variable
    print(i)

friends = ['ella','alice','jessie']
for friend in friends:  #iterate的list可以是string，iterate variable也可以命名的更make sense
    print("happy new year!: ",friend)

###finding the largest value
largest_so_far = -1  #先set一个初始值
for num in [9,41,12,3,74,15]:
    if num > largest_so_far:  #相当于一一比较
        largest_so_far = num
    print(largest_so_far)
print('The largest is:',largest_so_far) #最后print结果
