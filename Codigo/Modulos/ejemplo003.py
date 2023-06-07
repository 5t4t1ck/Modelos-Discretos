from twitter import *
import api_Key

token = api_Key.token
token_secret = api_Key.token_secret
consumer_key = api_Key.consumer_key
consumer_secret = api_Key.consumer_secret

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# to pass in the GET/POST parameter `id` you need to use `_id`
t.statuses.show(_id=1234567890)