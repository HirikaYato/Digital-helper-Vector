import vk_api as vk_api
import random
import json
import time
import botLib
import requests
from main import get_response
import random_responses

from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll,VkBotMessageEvent,VkBotEvent
from vk_api.requests_pool import VkRequestsPool,RequestResult


#Фунцкия для обработки вопросов
def question(event:VkBotMessageEvent):

    print('Launch scenary: ', question.__name__)

    #Обработка нажатия кнопки
    if event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='question':
       
        botLib.session.method('messages.send',{
                    'user_id': event.object['user_id'],
                    'random_id': random.randint(4,1000)+time.localtime().tm_sec,
                    'keyboard': botLib.keyboard_question.get_keyboard(),
                    'message': 'Задайте интересующий вас вопрос и я постараюсь на него ответить'
                    })
        
        #Прослушаивание и обработка событий с сервера
        for events in botLib.bot_longpoll.listen():
            if events.type==VkBotEventType.MESSAGE_NEW and events.from_user:
                botLib.session.method('messages.send',{

                    'user_id': events.message['from_id'],
                    'random_id': random.randint(5,1000)+time.localtime().tm_sec,
                    'message': 'Обработка запроса'

                    })
                if (events.message['text']!=None or events.message['text']!=' '):
                    
                    #Генерация ответа от бота
                    answer=get_response(events.message['text'])

                    if type(answer) !=str and answer['response_type']=='question':

                            botLib.session.method('messages.send',{

                                'user_id': events.message['from_id'],
                                'random_id': random.randint(12,1000)+time.localtime().tm_sec,
                                'keyboard': botLib.keyboard_question.get_keyboard(),
                                'message': answer['bot_response'][:len(answer['bot_response'])-2]

                                })

                    elif type(answer) !=str and answer['response_type']=='Bye':
                        botLib.session.method('messages.send',{

                                'user_id': events.message['from_id'],
                                'random_id': random.randint(7,1000)+time.localtime().tm_sec,
                                'keyboard': botLib.keyboard_question.get_keyboard(),
                                'message': answer['bot_response'][:len(answer['bot_response'])-2]

                                })

                    else:
                        botLib.session.method('messages.send',{

                            'user_id': events.message['from_id'],
                            'keyboard': botLib.keyboard_question.get_keyboard(),
                            'random_id': random.randint(9,1000)+time.localtime().tm_sec,
                            'message': answer
                        })

            elif events.type==VkBotEventType.MESSAGE_EVENT and events.object['payload'][0]=='back':
                botLib.writeInFile(main.__name__,events.object['user_id'])
                botLib.session.method('messages.sendMessageEventAnswer',{
                        'event_id':events.object['event_id'],
                        'user_id':events.object['user_id'],
                        'peer_id':events.object['peer_id'],
                        'event_data':json.dumps( botLib.session.method('messages.send',{

                            'user_id': events.object['user_id'],
                            'random_id': random.randint(50,1000)+time.localtime().tm_sec,
                            'keyboard': botLib.keyboard_start.get_keyboard(),
                            'message': 'Приветствую вас!\nЧто вы желаете выполнить?'
                        }))
                    })
            if event.type != VkBotEventType.MESSAGE_TYPING_STATE:
                botLib.sPrintLog(events,True)

    #Проверка, в случае перезапуска бота
    else:
        for events in botLib.bot_longpoll.listen():
            if events.type==VkBotEventType.MESSAGE_NEW and events.from_user:
                botLib.session.method('messages.send',{

                    'user_id': events.message['from_id'],
                    'random_id': random.randint(11,1000)+time.localtime().tm_sec,
                    'message': 'Обработка запроса'

                    })
                
                if (events.message['text']!=None or events.message['text']!=' '):

                    #Генерация ответа от бота
                    answer=get_response(events.message['text'])

                    if type(answer) !=str and answer['response_type']=='question':

                            botLib.session.method('messages.send',{

                                'user_id': events.message['from_id'],
                                'random_id': random.randint(18,1000)+time.localtime().tm_sec,
                                'keyboard': botLib.keyboard_question.get_keyboard(),
                                'message': answer['bot_response'][:len(answer['bot_response'])-2]

                                })
                            
                    elif type(answer) !=str and answer['response_type']=='Bye':
                        botLib.session.method('messages.send',{

                                'user_id': events.message['from_id'],
                                'random_id': random.randint(24,1000)+time.localtime().tm_sec,
                                'keyboard': botLib.keyboard_question.get_keyboard(),
                                'message': answer['bot_response'][:len(answer['bot_response'])-2]

                                })

                    else:
                        botLib.session.method('messages.send',{

                            'user_id': events.message['from_id'],
                            'random_id': random.randint(13,1000)+time.localtime().tm_sec,
                            'keyboard': botLib.keyboard_question.get_keyboard(),
                            'message': answer
                        })
                        
            elif events.type==VkBotEventType.MESSAGE_EVENT and events.object['payload'][0]=='back':
                botLib.writeInFile(question.__name__,events.object['user_id'])
                botLib.session.method('messages.sendMessageEventAnswer',{
                        'event_id':events.object['event_id'],
                        'user_id':events.object['user_id'],
                        'peer_id':events.object['peer_id'],
                        'event_data':json.dumps( botLib.session.method('messages.send',{

                            'user_id': events.object['user_id'],
                            'random_id': random.randint(50,1000)+time.localtime().tm_sec,
                            'keyboard': botLib.keyboard_start.get_keyboard(),
                            'message': 'Приветствую вас!\nЧто вы желаете выполнить?'
                        }))
                    })
            if event.type != VkBotEventType.MESSAGE_TYPING_STATE:
                botLib.sPrintLog(events,True)


def main():
    print("BOT STARTED")

    print('Launch scenary: ', main.__name__)

    #Прослушаивание и обработка событий с сервера
    for event in botLib.bot_longpoll.listen():
        
        if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Начать':
            botLib.writeInFile_start(event.message['from_id'],event.message['from_id'],'user')
            botLib.session.method('messages.send',{

                'user_id': event.message['from_id'],
                'random_id': random.randint(1,1000)+time.localtime().tm_sec,
                'attachment': 'photo-223836799_456239019',
                'message': 'Привет!) Это команда [Vector]. Сейчас у нас идет тестирование кейса [Хакатон: Лидеры Цифровой трансформации].\nЕсли вы хотите по взаимодействовать с ботом по этому кейсу, то можете отправить ему любое приветственное слово (привет, хай, хей и т.д).'

                })  
        
        #Обработка основных сообщений для бота
        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user:
            botLib.session.method('messages.send',{

                'user_id': event.message['from_id'],
                'random_id': random.randint(2,1000)+time.localtime().tm_sec,
                'message': 'Обработка запроса'

                })
            
            if (event.message['text']!=None or event.message['text']!=' '):
                
                #Генерация ответа от бота
                answer=get_response(event.message['text'])

                #Отправка ответа ботом
                if event.message['text'].lower() in ["привет","хей","хай","доброе утро","добрый день","добрый вечер",]:
                        
                        botLib.session.method('messages.send',{

                            'user_id': event.message['from_id'],
                            'random_id': random.randint(3,1000)+time.localtime().tm_sec,
                            'keyboard': botLib.keyboard_start.get_keyboard(),
                            'message': "Приветствую вас!\nЧто вы желаете выполнить?"

                            })
                        
                elif type(answer) !=str and answer['response_type']=='Bye':
                        botLib.session.method('messages.send',{

                                'user_id': event.message['from_id'],
                                'random_id': random.randint(7,1000)+time.localtime().tm_sec,
                                'message': answer['bot_response'][:len(answer['bot_response'])-2]

                                })

                else:
                    botLib.session.method('messages.send',{

                        'user_id': event.message['from_id'],
                        'random_id': random.randint(8,1000)+time.localtime().tm_sec,
                        'message': random_responses.random_string()
                    })

        
        #Обработка нажатия inline кнопки
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='question':
            botLib.writeInFile(question.__name__,event.object['user_id'])
            botLib.session.method('messages.sendMessageEventAnswer',{
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id']
                })
            botLib.sPrintLog(event,True)
            question(event)


        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='back':
            botLib.writeInFile(question.__name__,event.object['user_id'])
            botLib.session.method('messages.sendMessageEventAnswer',{
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                    'event_data':json.dumps( botLib.session.method('messages.send',{

                        'user_id': event.object['user_id'],
                        'random_id': random.randint(13,1000)+time.localtime().tm_sec,
                        'keyboard': botLib.keyboard_start.get_keyboard(),
                        'message': 'Приветствую вас!\nЧто вы желаете выполнить?'
                    }))
                })
            botLib.sPrintLog(event,True)

        #Вывод и запись логов
        if event.type != VkBotEventType.MESSAGE_TYPING_STATE:
            botLib.sPrintLog(event,True)




main()