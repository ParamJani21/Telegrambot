import requests
import webbrowser
import re

def change(url):
    #print(url)
    y = url.find("tag")
    z = url[0:y]
    f = z + "tag=mpjani-21"
    return f
#add an input flield of chat id here  and take chat id from json file
base_url = "https://api.telegram.org/bot6319772181:AAG3WXTSrsC3Zpraxl2HdKk9ZZEqJBv3BmE"


# def read_msg():
parameter = {
    "offset": "482396017"
}
resp = requests.get(base_url + "/getUpdates", data=parameter)
data = resp.json()
print(data)
for result in data["result"]:
    if "message" in result and "text" in result["message"] and "id" in result["message"]["chat"] and "chat" in result["message"]:
        x = result["message"]["text"]
        t = result["message"]["chat"]["id"]
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[^\(\), ][ (?:%[0-9a-fA-F][0-9a-fA-F])+', x)

#print(t)
#print(s)
if not url:
    None
else:
    c = " ".join(url)
    print(c)
    s = x.find("https://")
    o = x[0:s]
    #print(url)
    #print(o)

    if 'tag' in c:
        a = change(c)
    #print(a)
    else:
        for z in url:
            r = requests.get(z, allow_redirects=False)
        try:
            y = r.headers['location']
            a = change(y)
        except KeyError:
            print(url, "page not available")


    q = {o,a}

    
        


def send_msg(chat_id,text):
    params = {
        "chat_id":chat_id,
        "text":text
     }
    response = requests.post(base_url +"/sendMessage",params)
    
#for i in q:
#    print("fjwofi"+i)

send_msg(-1001953949660,o+a)