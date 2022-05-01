import xml.etree.ElementTree as ET
input = '''
一长段XML
'''

stuff = ET.fromstring(input)  #把XML变成python懂的object(like a tree
lst = stuff.findall('users/user')  #找到所有包含users或user的tags
print('user count:', len(lst)) #有多少user tags
for item in lst:
    