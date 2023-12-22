#Алгоритм для ввода данных в bot.json

import json
import re

uinput='Здравствуйте!В районе к сожалению, не проходит чемпионат района по мини-футболу, ограничиваются проведением спартакиады для работников!На которой играют только работники компании состоящие в профсоюзе !Если Мирный играет, то отдаленные районы могут позволить себе выездные соревнования 1раз в год и то не все('
bresponse="""Я не обладаю достаточной информацией, чтобы правильно ответить на данный вопрос. Обратитесь по этому вопросу к администрации, с помощью: номера телефона, почты или личном визите. С уважением, Ваш бот помощник."""
keyWord='не проходит чемпионат района по мини-футболу профсоюзе'  

#нельзя посещать сыном ребенком 5 лет

#Шаблон для заполнения
q={
    "response_type": "question",
    "user_input": [],
    "bot_response":  "",
    "required_words": []
  }

#Чтение файла, добавление нового словаря
with open ('bot.json','r',encoding='utf-8') as bot:
    data=json.load(bot)

uinput=uinput.lower()
keyWord=keyWord.lower()
split_keyWord=re.split(r'\s+|[,;?!.-]\s*',keyWord)

q['user_input']=uinput.split()
q['bot_response']=bresponse

for i in split_keyWord:
  q['required_words'].append(i)
  
data.append(q)


#Перезапись исходника (с добавлением новых данных)
with open ('bot.json','w',encoding='utf-8') as bot:
    bot.write(json.dumps(data,ensure_ascii=False,indent=2))