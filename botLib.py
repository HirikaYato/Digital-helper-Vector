import vk_api as vk_api
from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll,VkBotMessageEvent,VkBotEvent
from vk_api.keyboard import VkKeyboard,VkKeyboardButton,VkKeyboardColor
from vk_api.upload import VkUpload
from vk_api.requests_pool import VkRequestsPool,RequestResult
from dotenv import load_dotenv
import datetime
import json
import re
import os


load_dotenv()
#Инициализация сессии бота при помощи токена
session=vk_api.VkApi(token=os.getenv('BOT_TOKEN'))
#Создание объекта, для обработки событий от сервера
bot_longpoll=VkBotLongPoll(session,'223836799',10)





group_id='223836799'

state_scenary={'state':''}


user={'user_id':'',
        'peer_id':'',
        'state':'',
        'ban':'',
        'permission':''
        }


userInfo_val={
    'group_id':group_id,
    'user_id':[]
    }


#Проверить сообщение на категорию question
def num_check(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string[-1]):
        return True
    else:
        return False


#Получить id 
def getUserId(userID:int):
    """
    userID: id пользователя
    """

    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                return file_user
            

#Забанить пользователя
def banUser(userID:int):
    """
    userID: id пользователя
    """

    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                dataUser['user_id'][file_user]['ban']=True
    
    with open ('userInfo.json','w') as file:
        file.write(json.dumps(dataUser))
        print(f'[LOG] [{datetime.datetime.now()}] User: {userID} was ban')


#Разабанить пользователя
def unBanUser(userID:int):
    """
    userID: id пользователя
    """

    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                dataUser['user_id'][file_user]['ban']=False
    
    with open ('userInfo.json','w') as file:
        file.write(json.dumps(dataUser))
        print(f'[LOG] [{datetime.datetime.now()}] User: {userID} was unban')


#Проверить пользователя на бан
def checkUserOnBan(userID:int):
    """
    userID: id пользователя
    """

    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                if dataUser['user_id'][file_user]['ban']==True:
                    return True
                else:
                    return False
            

#Получить права пользователя
def getUserPermission(userID:int):
    """
    Получить статус прав пользователя

    userID: id пользователя
    """
    
    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                return dataUser['user_id'][file_user]['permission']
            

#Ф-ция для получения сценария, в котором сейчас находится пользователь
def getUserState(userID:int):
    """
    Получить стутус нахождения в сценарии

    userID: id пользователя
    """

    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                return dataUser['user_id'][file_user]['state']


#Ф-ция для изменения прав пользователя
def setUserPermission(userID:int,permission:str):
    """
    Назначить права пользователю

    userID: id пользователя
    state: название сценария, в котором вы находитесь
    """
    
    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                dataUser['user_id'][file_user]['permission']=permission
    
    with open ('userInfo.json','w') as file:
        file.write(json.dumps(dataUser))
        print(f'[LOG] [{datetime.datetime.now()}] User: {userID} was change permission on [{permission}]')


#Ф-ция для вставки ссылки на документ в ответ бота
def attachUrl(url:str):
    url=url

    with open('ref.json','r') as file:
            data=json.load(file)
    
    for i in range(len(data)):
        if (data[str[i]==url]):
            return data[str[i]]


#Изменить стутус сценария пользователя
def writeInFile(state:str,userID:int):
    """
    Изменение информации о пользователе

    userID: id пользователя
    state: название сценария, в котором вы находитесь
    """

    with open('userInfo.json','r') as file:
        dataUser = json.load(file)
        
    if userID==170852963:
        user['user_id']=userID
        user['peer_id']=userID
        user['state']='start'
        user['ban']=False
        user['permission']='admin'
    
    else:
        user['user_id']=userID
        user['peer_id']=userID
        user['state']='start'
        user['ban']=False
        user['permission']='user'

    with open('userInfo.json','w') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                dataUser['user_id'][file_user]=user
                break
            else:
                continue
        file.write(json.dumps(dataUser))


#Первичное внесение пользователя
def writeInFile_start(user_id,peer_id,permission):
    """
    permission: уровень доступа (права) пользователя
    """

    if user_id==170852963:
        user['user_id']=user_id
        user['peer_id']=peer_id
        user['state']='start'
        user['ban']=False
        user['permission']='admin'
    
    else:
        user['user_id']=user_id
        user['peer_id']=peer_id
        user['state']='start'
        user['ban']=False
        user['permission']=permission

    with open('userInfo.json','w') as file:
        file.write(json.dumps(userInfo_val))


    with open('userInfo.json','r') as file:
        dataUser = json.load(file)
    
    dataUser['user_id'].append(user)
    with open('userInfo.json','w+') as file:
        file.write(json.dumps(dataUser))


#Вывод и запись логов
def sPrintLog(event:VkBotMessageEvent, save:bool):
    """
    Ведение логов с возможность записи их в файл

    event: событие типа VkBotMessageEvent
    save: сохранять ли данный лог при выводе
    pathFile: путь к файлу лога, в который нужно сохранять
    """

    check=session.method('messages.getLongPollServer',{'need_pts':1,'group_id':event.group_id,'lp_version':3})
    long=session.method('messages.getLongPollHistory',{'ts':check['ts'], 'group_id': event.group_id,'preview_length':0})

    if (long['messages']['count']>0):
        pass

    with open('userInfo.json','r') as file:
        dataUser_r = json.load(file)


    
    if event.type== VkBotEventType.MESSAGE_NEW:
        userIndex=getUserId(event.message["from_id"])
    elif event.type==VkBotEventType.MESSAGE_REPLY:
        userIndex=getUserId(event.object["peer_id"])
    elif event.type==VkBotEventType.MESSAGE_EVENT:
        userIndex=getUserId(event.object["user_id"])

    if event.type==VkBotEventType.MESSAGE_NEW:
        print(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.message["from_id"]} | Scenary: {dataUser_r["user_id"][userIndex]["state"]} | Event: {event.type} | Text: {event.message["text"]}')
    elif event.type==VkBotEventType.MESSAGE_EVENT:
        print(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.object["user_id"]} | Scenary: {dataUser_r["user_id"][userIndex]["state"]} | Event: {event.type} | Payload: {event.object["payload"]}')

    if (save):
        with open('BotLog.txt','a',encoding='utf-8') as file:
            if event.type==VkBotEventType.MESSAGE_NEW:
                file.writelines(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.message["from_id"]} | Scenary: {dataUser_r["user_id"][userIndex]["state"]} | Event: {event.type} | Text: {event.message["text"]}\n')
            elif event.type==VkBotEventType.MESSAGE_EVENT:
                file.writelines(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.object["user_id"]} | Scenary: {dataUser_r["user_id"][userIndex]["state"]} | Event: {event.type} | Payload: {event.object["payload"]}\n')



#Объект клавиатуры, сценария "Старт"
keyboard_start=VkKeyboard(inline=True) #Callback_button - для перехода между сценариями; usual_button - для взаимодействия внутри данного сценария
#Объект клавиатуры, сценарий "Вопросы"
keyboard_question=VkKeyboard(inline=True)
#Объект для составления и обработки запросов
request_pool_api=VkRequestsPool(session)
#Объект, характеризующий результат запроса
pool_result=RequestResult()
#Объект для загрузки данных
upload=VkUpload(session)


keyboard_start.add_callback_button('Задать вопрос',VkKeyboardColor.SECONDARY,['question'])
keyboard_start.add_line()
keyboard_start.add_openlink_button('Просмотреть указы','https://www.xn----7sbab7amcgekn3b5j.xn--p1ai/administratsiya-mo/postanovleniya-i-rasporyazheniya-glavy-mr/',['decree'])

keyboard_question.add_callback_button('Назад',VkKeyboardColor.NEGATIVE,['back'])
