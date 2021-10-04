
import pickle
import os
import requests
from twilio.rest import Client
from py_imessage import imessage
from bs4 import BeautifulSoup
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime
from cal_setup import get_calendar_service
from datetime import datetime, date, time

Message = "Good Morning!"
account_sid = 'ACd6fc7fc254f09532e796c03fc79a91c6'
auth_token = 'f525d7b2211d732f72188102a4c0cd96'
client = Client(account_sid, auth_token)
#weather
weather = BeautifulSoup(requests.get("https://weather.gc.ca/city/pages/ab-50_metric_e.html").content,features="lxml")
tempS = (weather.find("span", attrs={'class': "wxo-metric-hide"}).text)
windS = (weather.find("dd", attrs={'class': "longContent mrgn-bttm-0 wxo-metric-hide"}).text)
temp = int(tempS[:-2])
for i in windS.split():
    if i.isdigit():
        wind=int(i)
condition=''
def weather(temp,wind):
    if temp<=10:
        condition='Wear a heavy jacket! It is very cold outside.'
    if temp>10 and temp<=14:
        condition='Wear a light jacket, it might get a little cold.'
    if temp>14 and temp<=23:
        condition='It is very nice outside. Have a wonderful day!.'
    if temp>23 and temp<=27:
        condition= 'It could get hot today. Wear light clothing'
    if temp>27:
        condition= 'Heat warning! Dress lightly and drink plenty of water'

    if temp<=14 and wind>=8 and wind<24:
        condition= "It is windy wear a jacket"
    if wind>28:
        condition = condition+ ' Winds are dangerously high today! Be careful!'
    return condition
Message= Message + ' ' + weather(temp,wind)

#calender
today_beginning = datetime.combine(date.today(), time())
today_end = datetime.combine(date.today(), time.max)
todo = {}
#def main():
message= ''
service = get_calendar_service()
   # Call the Calendar API
now = today_beginning.isoformat() + 'Z' # 'Z' indicates UTC time
end = today_end.isoformat() + 'Z'
events_result = service.events().list(
    calendarId = 'primary', timeMin = now,
    timeMax = end, singleEvents = True,
    orderBy = 'startTime').execute()
events = events_result.get('items', [])

if not events:
    message= message + 'You do not have any events scheduled for today'
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
       
    todo.update({event['summary'] : start[11:19]})
   
       

#if __name__ == '__main__':
  # main()
if len(todo) != 0:
    message= message+ 'You have several events scheduled for today:'
    for key in todo:
        message= message + '\n'+  key + ' at ' + todo.get(key)

print(Message + '\n' + message)


#message = client.messages \
            #    .create(
             #        body=Message,
             #        from_='+14695303556',
             #        to='+12025158028'
               #  )
    
        
    
    

    


