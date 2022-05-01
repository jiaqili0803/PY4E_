#######ex1
#prompts for a file name
#opens that file
#reads through the file
#print the contents of the file in upper case
#words.txt
##########
fname = input('plz enter file name: ')
file = open(fname)
for line in file:
    line = line.rstrip()
    print(line.upper())


#######ex2
#prompts for a file name
#opens that file and reads through the file,
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines
#extract the floating point values from each of the lines
#compute the average of those values
#produce an output as shown below:
#Average spam confidence: 0.7507185185185187
#mbox-short.txt
#######

print('======================ex2================')
fname = input('plz enter filename: ')
file = open(fname)
count = 0
total = 0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        values = float(line[21:])
        total = total + values
print('Average spam confidence:',total/count)
