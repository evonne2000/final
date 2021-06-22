from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import requests
from bs4 import BeautifulSoup
import sys
sys.path.append('/Users/michael/my_py_scripts')


line_bot_api = LineBotApi('RTXNIZl51aaPv9sXurBVF4V4KDkhwZT6jLHz1yfOCKZV6oilyUQRP0um+xuKkZqHgd+SR95/IXvHdxSjgbMX034rPYdRAtK/CnFtPFFoJdV0Ty3S5Mv9DeYwdtMpHVZ2bsJNZpFJuyROiPQKEAYSbwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ac580e7fc96fd3869e7fc48c941c7563')

def getinfo(name):
    url = "https://zh.wikipedia.org/wiki/" + name
    html = requests.get(url)
    html.encoding = "UTF-8"
    sp = BeautifulSoup(html.text, "lxml")
    #print(sp.find(class_= 'nickname'))
    #print(sp.find_all(class_='nickname'))
    nickname_class = sp.find_all(class_='nickname')
    #print(nickname)
    fullname = str(nickname_class[0])
    fullname = fullname.split('<')
    fullname = fullname[1].split('>')
    fullname = fullname[1]
    print(fullname)
    nick = 0
    if len(nickname_class) >= 3:
        nickname = str(nickname_class[2])
        nickname = nickname.split('<')
        nickname = nickname[1].split('>')
        nickname = nickname[1]
        nick = 1
        print(nickname)
    bd = sp.find(class_= "bday")
    bd = str(bd).split('<')
    bd = bd[1].split('>')
    bd = bd[1]
    print(bd)
    role = sp.find(class_="role")
    role = str(role).split('<')
    role = role[1].split('>')
    role = role[1]
    print(role)

    organ = 0
    orgs = sp.find_all(class_="org")
    if orgs != None:
        orgs = str(orgs).split(',')
        organization = []
        for org in orgs:
            tmp = org.split('<')
            tmp = tmp[2].split('>')
            tmp = tmp[1]
            if tmp not in organization:
                organization.append(tmp)
        organizations = ""
        for s in organization:
            if s != organization[0]:
                organizations += ','
            organizations += s
            organ = 1
        print(organizations)
    message = "本名" + fullname + '\n'
    if nick == 1:
        message = "綽號" + nickname + '\n'
    message = "生日" + bd + '\n'
    if organ == 1:
        message = "合作公司（經紀公司或唱片公司）" + organizations + '\n'
    return message
    #print(fullname)
    #print(sp.select('.nickname'))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    #print('bbb')
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    #print('ccc')
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    name = mtext.strip()
    information=getinfo(name)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=information))

if __name__ == "__main__":
    app.run()