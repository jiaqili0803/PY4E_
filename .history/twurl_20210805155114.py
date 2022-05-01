#twurl.py
import urllib.error
import urllib.parse
import urllib.request

import oauth 

import hidden

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

#通过oauth返回我们想要的具体的，根据输入的(url, parameters)补全的url
def augment(url, parameters):
    #make a request
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    #sign the request
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    #return an url
    return oauth_request.to_url()

#just a test
def test_me():
    print('* Calling Twitter...')
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
                  {'screen_name': 'drchuck', 'count': '2'})
    print(url)
    connection = urllib.request.urlopen(url)
    data = connection.read()
    print(data)
    headers = dict(connection.getheaders())
    print(headers)
