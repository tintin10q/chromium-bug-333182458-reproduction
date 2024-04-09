
import requests, webpush, zlib, json, base64


# Replace the ... with what you copied from https://localhost:8000, then run python push.py
# It should look something like this:
# subscription = {"endpoint":"https://fcm.googleapis.com/fcm/send/....","keys":{"p256dh":"...","auth":"..."}}

subscription = ... 

wp = webpush.WebPush(private_key="./push_private_key.pem", public_key="./push_public_key.pem", subscriber="test@gmail.com")

subscription = webpush.WebPushSubscription.model_validate(subscription)

data = {"data": {"body": "a body", "title": "A title", "type": "announcement"}}
data = json.dumps(data).encode("utf-8")
data = zlib.compress(data) # <--- HERE WE COMPRESS THE DATA 

# The event.data is null in the push event handler if we don't base64 encode it. 
# Uncomment the line below and observe that the data is no longer null in the push event handler
# data = base64.encodebytes(data) 

print("Sending", len(data), "bytes")

message = wp.get(data, subscription=subscription)


requests.post(subscription.endpoint, data=message.encrypted, headers=message.headers)