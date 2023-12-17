#Алгоритм для ввода данных в bot.json

import json

uinput='Ваш вопрос'
bresponse="""Желаемый ответ бота"""

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

q['user_input']=uinput.split()
q['bot_response']=bresponse
data.append(q)


#Перезапись исходника (с добавлением новых данных)
with open ('bot.json','w',encoding='utf-8') as bot:
    bot.write(json.dumps(data,ensure_ascii=False,indent=2))