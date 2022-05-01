#if
print("===if loop===")
x=5
if x < 10:   #if后有colon冒号
	print("small") #下面缩进的命令，满足if就执行 不满足就跳过
if x > 20:
	print("large")
print("finish")

#nested
print("===nested===")
for i in range(5):
	print(i)
	if i > 2:
		print("bigger than 2")
	print("done with i",i)
print("all done!！")

#two way desision
print("===if else===")
x = 4
if x > 2:
	print("bigger")
else:
	print('smaller')
print("all done")

#多选一
x = 11
print("===elif===")
if x < 2:
	print("small")
elif x < 10:
	print("medium")
else:
	print("big")
print("all done")

#上保险 try except 避免traceback
print("===try except===")
a = "Hi"
try:
	b = int(a)  #error，但可以执行except
except:
	b = -1
print("first",b)

a = "123"
try:
	b = int(a)  #执行了，except就skip了
except:
	b = -1
print("second",b)

#ex1
print('===ex1===')
hours = input("Enter your hours:")
rate = input("Enter your rate:")
h = float(hours)
if h > 40:
	pay = float(rate)*1.5*(h-40)+float(rate)*40
else:
	pay = h*float(rate)
print(pay)
#ex2 if user input a nonnumerical
print('===ex2===')
hours = input("Enter your hours:")
rate = input("Enter your rate:")
try:
	h = float(hours)
	r = float(rate)
except:
	print("plz enter numeric input!!!")
	quit()  #不会执行下面的
if h > 40:
	pay = r*1.5*(h-40)+r*40
else:
	pay = h*r
print(pay)
