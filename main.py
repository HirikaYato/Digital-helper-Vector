import json
import re
import random_responses
from bs4 import BeautifulSoup
import requests

#((required_score/len(required_words))*100) >= ((len(required_words)/2)/len(required_words)*100)

# Load JSON data
def load_json(file):
    with open(file, encoding='utf-8') as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("bot.json")
#Store url
dic={'0':'/administratsiya-mo/postanovleniya-i-rasporyazheniya-glavy-mr/24719/'}


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

    
        percent=(required_score/len(required_words))*100
        score_list.append(percent)

    best_response = max(score_list)
    response_index = score_list.index(best_response)
    # Check if input is empty
    if input_string == "":
        return "Пожалуйста, напишите что нибудь"

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]

    return random_responses.random_string()

#Function for updating ref.json in case of adding new documentation.
def writeRefInFile():

    url='https://www.xn----7sbab7amcgekn3b5j.xn--p1ai/administratsiya-mo/postanovleniya-i-rasporyazheniya-glavy-mr/'

    key=0

    r=requests.get(url)
    ba=BeautifulSoup(r.content,"html.parser")
    main=ba.find('div','postanovlenie')

    with open('ref.json','r') as file:
            data=json.load(file)

    for ref in main.find_all('a'):
            name = ref['href']
            dic[str(key)]=f'https://www.xn----7sbab7amcgekn3b5j.xn--p1ai{name}'
            key+=1

    data=dic

    with open('ref.json','w') as file:
            file.write(json.dumps(data,indent=1))
