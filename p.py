import telepot
from bs4 import BeautifulSoup
from telepot.loop import MessageLoop
import time
from pprint import pprint
import os
import requests
import urllib.request
bot = telepot.Bot('1284344621:AAHWm27jrCsz0ACzivSeeipjKNqLF68AZTk')
saveDir = './images/'
if not os.path.isdir(saveDir):
    os.mkdir(saveDir)
def handle(msg):
    if '/getinfo'or '/getinfo@hamradio_bot'==msg['text']:
        pprint(msg)
        chat_id = msg['chat']['id']
        from_id = msg['from']['id']
        get()
        bot.sendMessage(chat_id, '傳播資訊如下：')
        bot.sendPhoto(chat_id, open('./images/Congestus_con.jpg', 'rb'))
        os.remove('./images/Congestus_con.jpg')
    if '/about' ==msg['text']:
        pprint(msg)
        chat_id = msg['chat']['id']
        from_id = msg['from']['id']
        bot.sendMessage(chat_id, '本機器人由BX4ACP進行開發，這個服務為開源免費的，歡迎大家的使用。\n資料來源https://rigreference.com/solar\n計畫代號：式神project')
MessageLoop(bot, handle).run_as_thread()
def get():
    url = 'https://rigreference.com/solar/img/wide'
    response = requests.get(url)  # 使用header避免訪問受到限制
    soup = BeautifulSoup(response.content, 'html.parser')
    folder_path = './photo/'
    with open(saveDir + 'Congestus_con.jpg', 'wb') as f:
        f.write(response.content)
print("I'm listening...")
while 1:
    time.sleep(1)




