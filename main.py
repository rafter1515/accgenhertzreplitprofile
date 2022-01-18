import hmac
import base64
from hashlib import sha1
import os


def generate_device_Id():
    identifier = os.urandom(20)
    return ("32" + identifier.hex() + hmac.new(bytes.fromhex("76b4a156aaccade137b8b1e77b435a81971fbd3e"),
                                               b"\x32" + identifier, sha1).hexdigest()).upper()


import amino
import json
import threading
import wget
import requests
import heroku3
from new import emaill, passwordd, custompwd, chatlink, private, key, app_name, deviceid, nickname, replit
import urllib
import names
import random

lists=[]
cmlink=[]

t = open('cm.txt','r')
for m in t.read().splitlines():
    temp=m
    lists.append(str(temp))
t.close()
cl=amino.Client()

def findcm():
    for i in lists:
        try:
            fok=cl.get_from_code(i)
            cid=fok.path[1:fok.path.index("/")]
            cmlink.append(cid)
            print("\33[93;5;5m\33[93;5;234m ✓  "+ cid + "\33[0m\33[93;5;235m\33[93;5;5m \33[0m")
        except:
            print("Invalid link")
findcm()

def fancy_name():
    nm=''
    for i in names.get_first_name():
        nm=nm+i
    return nm

def images():
    img=''
    return img

def geticon(client):
    urlx=client.get_all_users(size=100).profile.icon
    for url in urlx:
        if url is None or url=="None":
            pass
        else:
          return url
          break

def restart():
    heroku_conn = heroku3.from_key(key)
    botapp = heroku_conn.apps()[app_name]
    botapp.restart()


client = amino.Client(deviceid)
client.login(emaill, passwordd)
bb = client.get_from_code(chatlink)
chatId = bb.objectId
cid = bb.path[1:bb.path.index("/")]
client.join_community(cid)
sub = amino.SubClient(comId=cid, profile=client.profile)
sub.join_chat(chatId)


def find():
    while True:
        p = sub.get_chat_messages(chatId=chatId, size=1).content
        # print(p)
        for j in p:
            g = j
        # print(g)
        l = f"{g}"
        length = str(len(l))
        if "6" == length:
            break
    return g

def change(em, ps, dv):
    try:
        print("start changing profile and name")
        clientus=amino.Client(deviceId=dv)
        clientus.login(email=em,password=ps)
        nick=("♣"+fancy_name()+"♥")
        search = "anime"
        response = requests.get(
            'http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=W05ZAoiUU7fHjXgOXU1Rs6No2CSULZUc')
        data = json.loads(response.text)
        gif_choice = random.randint(0, 50)
        image = data['data'][gif_choice]['images']['original']['url']
        if image is not None:
            filename="anime.png"
            urllib.request.urlretrieve(image, filename)
        img=open("anime.png","rb")
        clientus.edit_profile(icon=img,nickname=nick)
        print("\33[93;5;5m\33[93;5;234m ❮ Name changed ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m" + nick)
        print("\33[93;5;5m\33[93;5;234m ❮ ProfilePic changed ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m")
        try:
            clientus.configure(age=int(18),gender=("Male"))
            print("\33[93;5;5m\33[93;5;234m ❮ account configured ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m" + nick)
        except:
            print("\33[93;5;5m\33[93;5;234m ❮ account cant configured ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m" + nick)
    except Exception as y:
        print(y)
        print("\33[93;5;5m\33[93;5;234m ❮ ProfilePic cant changed ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m")
        pass
    try:
        for cid in cmlink:
            clientus.join_community(cid)
            print("\33[93;5;5m\33[93;5;234m ❮ joined to " + cid + " ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    except Exception as n:
        print(n)

password = custompwd
# client.devicee()
de = generate_device_Id()
client = amino.Client(de)

for _ in range(3):
    try:
        os.remove("code.png")
    except:
        pass
    dev = client.device_id
    email = client.gen_email()
    print(email)
    client.request_verify_code(email=email, dev=dev)
    link = client.get_message(email)
    wget.download(url=link, out="code.png")
    with open("code.png", "rb") as file:
        sub.send_message(chatId=chatId, fileType="image", file=file)
    p = sub.get_chat_messages(chatId=chatId, size=1).content
    code = find()

    try:
        client.register(email=email, password=password, nickname=nickname, verificationCode=code, deviceId=dev)
        d = {}
        d["email"] = str(email)
        d["password"] = str(password)
        d["device"] = str(dev)
        # t=json.dumps(d)
        print(d)
        requests.get(url=f"{replit}/api/save?email={str(email)}&password={str(password)}&device={str(dev)}")
        #change(email, password, dev)
    except Exception as l:
        print(l)
        pass

de = generate_device_Id()
client = amino.Client(de)
for _ in range(2):
    try:
        os.remove("code.png")
    except:
        pass
    dev = client.device_id
    email = client.gen_email()
    print(email)
    client.request_verify_code(email=email, dev=dev)
    link = client.get_message(email)
    wget.download(url=link, out="code.png")
    with open("code.png", "rb") as file:
        sub.send_message(chatId=chatId, fileType="image", file=file)
    code = find()

    try:
        client.register(email=email, password=password, nickname=nickname, verificationCode=code, deviceId=dev)
        d = {}
        d["email"] = str(email)
        d["password"] = str(password)
        d["device"] = str(dev)
        # t=json.dumps(d)
        print(d)
        requests.get(url=f"{replit}/api/save?email={str(email)}&password={str(password)}&device={str(dev)}")
        #change(email, password, dev)
    except Exception as k:
        print(k)
        pass

restart()
