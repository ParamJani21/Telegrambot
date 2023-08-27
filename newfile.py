from telethon import TelegramClient, events
import requests
from datetime import datetime
import re
import pytz

IST = pytz.timezone('Asia/Kolkata')
raw_TS = datetime.now(IST)
curr_date = raw_TS.strftime("%d-%m-%Y")
curr_time = raw_TS.strftime("%H:%M:%S")

def messageParse(msg):
    a2 = msg.replace("&","&amp")
    return a2

def change(url):
    y = url.find("tag")
    z = url[0:y]
    f = z + "tag=mpjani-21"
    return f

def send_mes(message):
    chatid="@abcd9925"
    message_1 = messageParse(message)
    params = {
        "chat_id": chatid,
        "text": message_1,
        "parse_mode": "HTML",
    }
    telegram_api = f"https://api.telegram.org/bot6489447040:AAE0DuiALHjvNvXjbb2Hb6rJt66udNj5yjI/sendMessage"
    tel_resp = requests.get(telegram_api,params=params)
    a = "null"
    print("message sent")
i=1

base_url = "https://api.telegram.org/bot6489447040:AAE0DuiALHjvNvXjbb2Hb6rJt66udNj5yjI"
parameter = {
        "offset": "482396017"
 }
resp = requests.get(base_url + "/getUpdates", data=parameter)
data = resp.json()
for result in data["result"]:
    if "message" in result and "text" in result["message"]:
            x = result["message"]["text"]
            url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[^\(\), ][ (?:%[0-9a-fA-F][0-9a-fA-F])+', x)
if not url:
        None
else:
        c = " ".join(url)
        s = x.find("https://")
        o = x[0:s]
        if 'tag' in c:
            a = change(c)
        else:
            for z in url:
                r = requests.get(z,allow_redirects=False)
            try:
                y = r.headers['location']
                a = change(y)
            except KeyError:
                print(url, "page not available")

msg = o+a
   
   
  #tag change and send 
send_mes(msg)
