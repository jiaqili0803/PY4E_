import json

#data is a string of big dict
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
