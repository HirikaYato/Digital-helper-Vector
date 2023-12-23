#Алгоритм для ввода данных в bot.json

import json
import re

uinput='Ваш вопрос'
bresponse="""Желаемый ответ бота"""
keyWord='ключ слова (через пробел, точку и т.д)'  

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