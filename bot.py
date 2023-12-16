import vk_api as vk_api
import random
import json
import time
import botLib
import requests
from main import get_response

from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll,VkBotMessageEvent,VkBotEvent
from vk_api.requests_pool import VkRequestsPool,RequestResult



def question(event:VkBotMessageEvent):

    print('Launch scenary: ', main.__name__)

    if event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='question':
       
        botLib.session.method('messages.send',{
                    'user_id': event.object['user_id'],
                    'random_id': random.randint(4,1000)+time.localtime().tm_sec,
                    'message': 'Задайте интересующий вас вопрос и я постараюсь на него ответить'
                    })
        
        for events in botLib.bot_longpoll.listen():
            if events.type==VkBotEventType.MESSAGE_NEW and events.from_user:
                botLib.session.method('messages.send',{

                    'user_id': events.message['from_id'],
                    'random_id': random.randint(5,1000)+time.localtime().tm_sec,
                    'message': 'Обработка текста...'

                    })
                if (events.message['text']!=None or events.message['text']!=' '):

                    answer=get_response(events.message['text'])

                    if (botLib.num_check(answer)):

                        botLib.session.method('messages.send',{

                            'user_id': events.message['from_id'],
                            'random_id': random.randint(7,1000)+time.localtime().tm_sec,
                            'message': answer[:len(answer)-2]

                            })
                    else:
                        botLib.session.method('messages.send',{

                            'user_id': events.message['from_id'],
                            'random_id': random.randint(9,1000)+time.localtime().tm_sec,
                            'message': answer
                        })

    else:
        for events in botLib.bot_longpoll.listen():
            if events.type==VkBotEventType.MESSAGE_NEW and events.from_user:
                botLib.session.method('messages.send',{

                    'user_id': events.message['from_id'],
                    'random_id': random.randint(11,1000)+time.localtime().tm_sec,
                    'message': 'Обработка текста...'

                    })
                
                if (events.message['text']!=None or events.message['text']!=' '):

                    answer=get_response(events.message['text'])

                    if (botLib.num_check(answer)):

                        botLib.session.method('messages.send',{

                            'user_id': events.message['from_id'],
                            'random_id': random.randint(12,1000)+time.localtime().tm_sec,
                            'message': answer[:len(answer)-2]

                            })
                    else:
                        botLib.session.method('messages.send',{

                            'user_id': events.message['from_id'],
                            'random_id': random.randint(13,1000)+time.localtime().tm_sec,
                            'message': answer
                        })


def main():
    print("BOT STARTED")

    print('Launch scenary: ', main.__name__)

    for event in botLib.bot_longpoll.listen():
        
        if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Начать':
            botLib.writeInFile_start(event.message['from_id'],event.message['from_id'],'user')
            botLib.session.method('messages.send',{

                'user_id': event.message['from_id'],
                'random_id': random.randint(1,1000)+time.localtime().tm_sec,
                'attachment': 'photo-223836799_456239019',
                'message': 'Привет!) Это команда [Vector]. Сейчас у нас идет тестирование кейса [Хакатон: Лидеры Цифровой трансформации].\nЕсли вы хотите повзаимодействовать с ботом по этому кейсу, то можете отправить ему любое приветственное слово.'

                })  
                
        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user:
            botLib.session.method('messages.send',{

                'user_id': event.message['from_id'],
                'random_id': random.randint(2,1000)+time.localtime().tm_sec,
                'message': 'Обработка текста...'

                })
            
            if (event.message['text']!=None or event.message['text']!=' '):

                answer=get_response(event.message['text'])

                if (botLib.num_check(answer)):

                    botLib.session.method('messages.send',{

                        'user_id': event.message['from_id'],
                        'random_id': random.randint(3,1000)+time.localtime().tm_sec,
                        'keyboard': botLib.keyboard_start.get_keyboard(),
                        'message': answer[:len(answer)-2]

                        })
                else:
                    botLib.session.method('messages.send',{

                        'user_id': event.message['from_id'],
                        'random_id': random.randint(8,1000)+time.localtime().tm_sec,
                        'keyboard': botLib.keyboard_start.get_keyboard(),
                        'message': answer
                    })
        

        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='question':
            botLib.writeInFile(question.__name__,event.object['user_id'])
            botLib.session.method('messages.sendMessageEventAnswer',{
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id']
                })
            botLib.sPrintLog(event,True)
            question(event)


        if event.type != VkBotEventType.MESSAGE_TYPING_STATE:
            botLib.sPrintLog(event,True)




main()