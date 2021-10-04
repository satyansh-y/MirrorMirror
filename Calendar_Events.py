
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime
from cal_setup import get_calendar_service
from datetime import datetime, date, time
import os
import requests
from twilio.rest import Client

#authentication---- 
#!!! Find out how new users get verification!!!

account_sid = 'ACd6fc7fc254f09532e796c03fc79a91c6'
auth_token = 'f525d7b2211d732f72188102a4c0cd96'
client = Client(account_sid, auth_token)
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

#events stored in array ^^^ can be used to print out on screeen

