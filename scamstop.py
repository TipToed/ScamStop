import os
try:
    import requests
except:
    try:
        os.system("pip3 install requests")
        import requests
    except:
        os.system("pip install requests")
        import requests
import random
import string
import json
import webbrowser


os.system("title ＳＣΛＭＳＴ♢Ｐ")

print(""" 
 _______ ______ _______ _______ _______ _______ _______ ______ 
|     __|      |   _   |   |   |     __|_     _|       |   __  )
|__     |   ---|       |       |__     | |   | |   -   |    __/
|_______|______|___|___|__|_|__|_______| |___| |_______|___|   
                                                             """)
print("By TIP TOED, and help of a lot of youtube videos")
Help = input("Do you need help[y/n]: ")
if Help == 'y':
    webbrowser.open("https://youtu.be/SvUqk683mSA?t=39")
    print("Press Ctrl+C to stop...")
    print("Or it will automatically stop after a 100 Requests")

URL_get = input("Enter Url The Page Sent Request To: ")
EMAIL_felid = input("Enter Email feild name: ")
PASSWORD_feild = input("Enter Password feild name: ")

chars = string.ascii_letters + string.digits + '!@#$$%^&*()'
random.seed = (os.urandom(1024))

url = URL_get

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))
    
    email = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(12))

    response = requests.post(url, allow_redirects=False, data={
        EMAIL_felid: email,
        PASSWORD_feild: password
    }).text

    print("------------SENT---------------------")
    print("Sending email %s and password %s" % (email, password))
    print("------------RESPONSE-----------------")
    print(response)
    print("-------------------------------------")

