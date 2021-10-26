import telepot, time, sys, json
from telepot.loop import MessageLoop

with open("token.json") as tkFile:
    token = json.load(tkFile)

telegram = telepot.Bot(token)
#telegram.getMe()
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        telegram.sendMessage(chat_id, msg['text'])
                
MessageLoop(telegram, handle).run_as_thread()
while 1:
    time.sleep(10)

    