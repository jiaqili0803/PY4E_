##每个API可能会有request amount限制，可能需要key，可能要付费
#twitter API就需要key来访问
import urllib.request, urllib.parse, urllib.error
import twurl  #通过oauth返回我们想要的具体url
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #用户输入行为
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    
    #通过oauth返回我们想要的具体url（twurl.py里面的augment函数用了oauth的方法们）
    #
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    
    #parse url
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    #json读成dict
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    #访问次数限制剩余
    headers = dict(connection.getheaders())  #urllib一般吃掉了header，这里我们补
    print('Remaining', headers['x-rate-limit-remaining']) #为了知道还能reques几次

    #具体extract
    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])