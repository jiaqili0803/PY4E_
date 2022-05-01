print('===========================ex1============================')
############ex1
#Open the file
#romeo.txt
#and read it line by line
#For each line,
#split the line into a list of words using the split()
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append it to the list.
#When the program completes,
#sort and print the resulting words in alphabetical order.
##########
new_list = []
file = open('romeo.txt')
for line in file:
    line_s = line.split()  #变成list of words
    #print(line_s)
    for each_word in line_s:
        if each_word in new_list:  #看是否已经存在
            continue
        new_list.append(each_word)

#result = new_list.sort() ##!!不能这么赋值搞！！
#print(result)

new_list.sort()
print(new_list) #sort() doesn't return a new list！！！所以print原new_list即可

print('===========================ex2============================')
#######ex2
#Open the file mbox-short.txt
#read it line by line.
#When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#You will parse the From line using split() and
#print out the second word in the line (i.e. the entire address of the person who sent the message).
#Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#Also look at the last line of the sample output to see how to print the count.
###########
count = 0
file = open('mbox-short.txt')
for line in file:
    if line.startswith('From '):
        line_s = line.split()
        print(line_s[1])
        count = count + 1
print('There were',count,'lines in the file with From as the first word')
