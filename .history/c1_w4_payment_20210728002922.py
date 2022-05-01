hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs1 = float(hrs)  #input进来是str需要转换成float
rate1 = float(rate)
pay = rate1 * hrs1
#print("Pay: "+ str(pay)) #float转成string 才能和string相加
#记得print
print("Pay:", pay)
