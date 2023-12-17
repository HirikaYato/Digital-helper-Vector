from bs4 import BeautifulSoup
import requests
import json

url='https://www.xn----7sbab7amcgekn3b5j.xn--p1ai/administratsiya-mo/postanovleniya-i-rasporyazheniya-glavy-mr/24623/'
key=0

with open('ref.json','r') as file:
     data=json.load(file)
    
for i in range(len(data)):
    if data[str(i)]==url:
         print('AAAAAAAAAAAAAAAAAA')
         break
