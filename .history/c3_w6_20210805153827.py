import json

#data is a string of big dict, may contain dict inside
data = '''{
    "name" : "Chunk",
    "phone" : {
        "type" : "intl",
        "number" : "5964163",
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)  #将json的string idict读成 python dict
print('Name:', info['name'])
print('Hide:', info['email']['hide'])  #有两层字典就这样定位两次

#input is a string of big list, may contain dict inside
input = '''[
    {"id" : "001",
    "x" : "2",
    "name" : "Chunk"
    },
    {"id" : "009",
    "x" : "7",
    "name" : "Chunk"
    }
]'''

information = json.loads(input)
print('count:', len(information))  #len = 2, list contains 2 dicts
for item in information: #因为是List所以需要loop;两个所以loop两次
    print('Name:', item['name'])
    print('Id:', item['id'])
