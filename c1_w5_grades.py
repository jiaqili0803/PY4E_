#ex3
print('===ex3===')
score = input("your score?")  #一定记得转换！
s = float(score)
if 0 <= s <= 1:
	if s < 0.6:
		print("F")
	elif s >= 0.9:
		print("A")
	elif s >= 0.8:
		print("B")
	elif s >= 0.7:
		print("C")
	elif s >= 0.6:
		print("D")
else:
	print("plz enter num between 0-1!!!")
