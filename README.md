# About the tool
This tool can be used to test APNs on your iOS app.
#Environment
- iOS app
- xcode
- .pem file
#Usage
- apns.py
```python
def APN(token, payload, theCertfile)
```
**token** is device token your app regitered  for APNS.
**payload** is a Jason format message that transfered from server to APNs then to clients.
**theCertfile** is the pem file bound to the Boundle Id of your app.
- push_ios.py
```python
def push(msg):
```
**msg** includes payload and token.
