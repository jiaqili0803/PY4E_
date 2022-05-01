###exercise
#text = "X-DSPAM-Confidence:    0.8475"
#find()
#slice
#excract number
#convert to float and print
#########################

text = "X-DSPAM-Confidence:    0.8475"
num_start = text.find('0')
num_end = text.find('5',num_start)
num = text[num_start : num_end+1]

#或者直接用：冒号，因为是尾部
num_start = text.find('0')
num = text[num_start:]

print(float(num))
