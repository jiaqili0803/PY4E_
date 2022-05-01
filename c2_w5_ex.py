#'''
###############ex1
#read through the mbox-short.txt
#figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and
#takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced,
#the program reads through the dictionary using a maximum loop to find the most prolific committer.
##########################

file = open('mbox-short.txt')
email_dict = dict()
for line in file:
    if line.startswith('From '):
        line_s = line.split()
        #print(line_s)
        email_dict[line_s[1]] = email_dict.get(line_s[1],0) + 1
#print(email_dict)

most_address = None
most_amount = None
for address,amount in email_dict.items():
    if most_amount is None or most_amount < amount:
        most_amount = amount
        most_address = address
print(most_address,most_amount)
