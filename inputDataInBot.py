#Алгоритм для ввода данных в bot.json

import json

uinput='Вопрос'
bresponse="""Желаемый ответ"""

q={
    "response_type": "question",
    "user_input": [],
    "bot_response":  "",
    "required_words": []
  }

with open ('bot.json','r',encoding='utf-8') as bot:
    data=json.load(bot)

uinput=uinput.lower()

q['user_input']=uinput.split()
q['bot_response']=bresponse
data.append(q)



with open ('bot.json','w',encoding='utf-8') as bot:
    bot.write(json.dumps(data,ensure_ascii=False,indent=2))