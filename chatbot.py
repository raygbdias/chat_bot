import json, sys, os, webbrowser
import subprocess as sp
from subprocess import Popen

class Severina():
    def __init__(self, name):
        try:
            memory = open(name + '.json', 'r')
        except FileNotFoundError:
            memory = open(name + '.json', 'w')
            memory.write('[["Severina"], {"oi": "Olá! Qual seu nome?", "tchau": "Tchau! Tchau!", "tudo bem": "estou otima e voce"}]')
            memory.close()
            memory = open(name + '.json', 'r')
        self.name = name
        self.known, self.phrases = json.load(memory)
        memory.close()
        self.historic = [None]
        
    def listen(self, phrase=None):
        if phrase == None:
            phrase = input('>: ')
        phrase = str(phrase)
        return phrase.lower()

    def think(self, phrase):
        def executa(url):
            platform = sys.platform
            link = phrase.replace('executa ', '')
            if 'win' in platform:
                os.startfile(link)
            if 'linux' in platform:
                try:
                    sp.Popen(link)
                except FileNotFoundError:
                    sp.Popen(['xdg-open', link])
            if 'darwin' in platform:
                #sp.run(['open', link], check=True)
                #sp.call(('open', link))
                #chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
                #webbrowser.get(chrome_path).open(link)  
                #webbrowser.open_new(link)
                #sp.Popen(['open',link])
                #sp.Popen(['start', 'link'],shell = True)
                #webbrowser.open(link, new=1)
                webbrowser.open(link)
                #os.system("open \"\" link")
                #os.system("start \"\" link")
                #webbrowser.open_new(link)
                #sp.Popen(['open',"/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome", "link"])
                #/Applications/Google Chrome.app
                #/Applications/Google Chrome.app/Contents/MacOS
                #sp.Popen("Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome")

        if phrase in self.phrases:
            return self.phrases[phrase]
        if phrase == 'aprende':
            return 'O que você quer que eu aprenda?'
        if phrase == 'tecmundo':
            return "https://www.tecmundo.com.br/"
        if "executa" in phrase:
            executa(phrase)
            return "aqui esta o url"
        
        # historic
        lastPhrase = self.historic[-1]
        if lastPhrase == 'Olá! Qual seu nome?':
            name = self.getName(phrase)
            response = self.answerName(name)
            return response
        if lastPhrase == 'O que você quer que eu aprenda?':
            self.key = phrase
            return 'Digite o que eu devo responder:'
        if lastPhrase == 'Digite o que eu devo responder:':
            response = phrase
            self.phrases[self.key] = response
            self.saveMemory()
            return 'Aprendido!'
        try:
            response = str(eval(phrase))
            return response
        except:
            pass
        return 'Não entendi...'
        
    def getName(self, name):
        if 'meu nome é ' in name:
            name = name[11:]
        name = name.title()
        return name

    def answerName(self, name):
        if name in self.known:
            if name != 'Severina':
                phrase = 'Eaew, '
            else:
                phrase = 'E se somos Severinas iguais em tudo na vida, morreremos de morte igual, mesma morte severina.'
        else:
            phrase = 'Muito prazer '
            self.known.append(name)
            self.saveMemory()
        return phrase + name + '!'
    
    def saveMemory(self):
        memory = open(self.name +'.json', 'w')
        json.dump([self.known, self.phrases], memory)
        memory.close()

    def speak(self, phrase):
        print(phrase)
        self.historic.append(phrase)