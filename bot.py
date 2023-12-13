import vk_api as vk_api
import random
import json
import time
import botLib
import requests

from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll,VkBotMessageEvent,VkBotEvent
from vk_api.requests_pool import VkRequestsPool,RequestResult


def main():
    print("BOT STARTED")

    print('Launch scenary: ', main.__name__)

    for event in botLib.bot_longpoll.listen():
        
        if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Начать':
            botLib.writeInFile_start(event.message['from_id'],event.message['from_id'],'user')
            botLib.session.method('messages.send',{

                'user_id': event.message['from_id'],
                'random_id': random.randint(10,1000)+time.localtime().tm_sec,
                'attachment': 'photo-223836799_456239019',
                'message': 'Сейчас идет тестирование кейса [Хакатон: Лидеры Цифровой трансформации].\nЕсли вы хотите повзаимодействовать с ботом, то можете отправить ему любой текст или слово "Старт".\nСпасибо за вниманиие!'

                })

        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Старт':
            # botLib.writeInFile(start.__name__,event.message['from_id'])
            botLib.session.method('messages.send',{

                'user_id': event.message['from_id'],
                'random_id': random.randint(1,1000)+time.localtime().tm_sec,
                'message': 'Начало сценария'

                })  
                
        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user:
            botLib.session.method('messages.send',{

                'user_id': event.message['from_id'],
                'random_id': random.randint(2,1000)+time.localtime().tm_sec,
                'message': 'Обработка текста...'

                })
            message=event.message['text']
            
            if (message!=None or message!=' '):
                print(message)

                botLib.session.method('messages.send',{

                    'user_id': event.message['from_id'],
                    'random_id': random.randint(3,1000)+time.localtime().tm_sec,
                    'message': f'Вы отправили сообщение: {message}'

                    })
        
        if event.type != VkBotEventType.MESSAGE_TYPING_STATE:
            botLib.sPrintLog(event,True)




main()