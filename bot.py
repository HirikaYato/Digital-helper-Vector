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
    if event.type==VkBotEventType.MESSAGE_EVENT and event.from_user and event.object['payload']=='question':
       
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
                message=events.message['text']
                
                if (message!=None or message!=' '):
                    mess=events.message['text']

                    botLib.session.method('messages.send',{

                        'user_id': events.message['from_id'],
                        'random_id': random.randint(6,1000)+time.localtime().tm_sec,
                        'message': get_response(mess.lower())

                        })

    else:
        for events in botLib.bot_longpoll.listen():
            if events.type==VkBotEventType.MESSAGE_NEW and events.from_user:
                botLib.session.method('messages.send',{

                    'user_id': events.message['from_id'],
                    'random_id': random.randint(7,1000)+time.localtime().tm_sec,
                    'message': 'Обработка текста...'

                    })
                message=events.message['text']
                
                if (message!=None or message!=' '):
                    mess=events.message['text']

                    botLib.session.method('messages.send',{

                        'user_id': events.message['from_id'],
                        'random_id': random.randint(8,1000)+time.localtime().tm_sec,
                        'message': get_response(mess.lower())

                        })


def decree (event:VkBotMessageEvent):
    pass



def appeal (event:VkBotMessageEvent):
    pass


#Разобраться в inline кнопке. Возможно listen на него не работает, т.к эти работа с сообщением (а не отображение клавиатуры)


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
            message=event.message['text']
            
            if (message!=None or message!=' '):
                mess=event.message['text']

                botLib.session.method('messages.send',{

                    'user_id': event.message['from_id'],
                    'random_id': random.randint(3,1000)+time.localtime().tm_sec,
                    'keyboard': botLib.keyboard_start.get_keyboard(),
                    'message': get_response(mess.lower())

                    })
        

        elif event.type==VkBotEventType.MESSAGE_EVENT and event.from_user and event.object['payload']=='question':
            botLib.writeInFile(question.__name__,event.object['user_id'])
            botLib.session.method('messages.sendMessageEventAnswer',{
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id']
                })
            question(event)

        elif event.type==VkBotEventType.MESSAGE_EVENT and event.from_user and event.object['payload']=='decree':
            botLib.writeInFile(decree.__name__,event.object['user_id'])
            botLib.session.method('messages.sendMessageEventAnswer',{
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id']
                })
            decree(event)
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.from_user and event.object['payload']=='appeal':
            botLib.writeInFile(appeal.__name__,event.object['user_id'])
            botLib.session.method('messages.sendMessageEventAnswer',{
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id']
                })
            appeal(event)


        if event.type != VkBotEventType.MESSAGE_TYPING_STATE:
            botLib.sPrintLog(event,True)




main()