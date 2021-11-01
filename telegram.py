import telepot, time, sys, json
from telepot.loop import MessageLoop
from chatbot import Severina

with open("token.json") as tkFile:
    token = json.load(tkFile)

telegram = telepot.Bot(token)
bot = Severina('luna')

#telegram.getMe()
def handle(msg):
    frase = bot.listen(phrase= msg['text'])
    response = bot.think(frase)
    bot.speak(response)
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    telegram.sendMessage(chat_id, response)
    #if content_type == 'text':
        #telegram.sendMessage(chat_id, msg['text'])
                
MessageLoop(telegram, handle).run_as_thread()
while 1:
    time.sleep(10)

    