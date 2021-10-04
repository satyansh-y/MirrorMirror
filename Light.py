import os
import sys
import os.path
import os
import requests
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime
from cal_setup import get_calendar_service
from datetime import datetime, date, time
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import termios
import tty
import pigpio
import time
from _thread import start_new_thread
import socket
import urllib.parse

RED_PIN   = 13
GREEN_PIN = 19
BLUE_PIN  = 37

red=pigpio.pi()
green=pigpio.pi()
blue=pigpio.pi()
#code to set individual pin brightness- change brightness value




#Tornado Folder Paths
settings = dict(
        template_path = os.path.join(os.path.dirname(__file__), "/Users/satyanshy/Documents/GitHub/MirrorMirror/template"),
        static_path = os.path.join(os.path.dirname(__file__), "/Users/satyanshy/Documents/GitHub/MirrorMirror/static")
        )

#Tonado server port
PORT = 80


class MainHandler(tornado.web.RequestHandler):
  def get(self):
     print("[HTTP](MainHandler) User Connected.")
     self.render("index.html")

        
class WSHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    print('[WS] Connection was opened.')

  def write_message(self, message):
    self.write_message("it is working")
  write_message(WSHandler, "hello")
  def on_message(self, message):
    print('[WS] Incoming message:', message)
    if message == "ON":
      print("working")
      #red.set_PWM_dutycycle(RED_PIN, 100)      
      #green.set_PWM_dutycycle(GREEN_PIN, 100)
      #blue.set_PWM_dutycycle(BLUE_PIN, 100)
      
    if message == "OFF":
      red.set_PWM_dutycycle(RED_PIN, 100)      
      green.set_PWM_dutycycle(GREEN_PIN, 100)
      blue.set_PWM_dutycycle(BLUE_PIN, 100)
      print("working")
    if message == "Red":
      red.set_PWM_dutycycle(RED_PIN, 255)      
      green.set_PWM_dutycycle(GREEN_PIN, 0)
      blue.set_PWM_dutycycle(BLUE_PIN, 0)
      print("working")
    if message == "Green":
      red.set_PWM_dutycycle(RED_PIN, 0)      
      green.set_PWM_dutycycle(GREEN_PIN, 255)
      blue.set_PWM_dutycycle(BLUE_PIN, 0)
      print("working")
    if message == "Blue":
      red.set_PWM_dutycycle(RED_PIN, 0)      
      green.set_PWM_dutycycle(GREEN_PIN, 0)
      blue.set_PWM_dutycycle(BLUE_PIN, 255)
      print("working")
    if message == "White":
      red.set_PWM_dutycycle(RED_PIN, 255)      
      green.set_PWM_dutycycle(GREEN_PIN, 255)
      blue.set_PWM_dutycycle(BLUE_PIN, 255)
      print("working")
    if message == "Yellow":
      red.set_PWM_dutycycle(RED_PIN, 255)      
      green.set_PWM_dutycycle(GREEN_PIN, 255)
      blue.set_PWM_dutycycle(BLUE_PIN, 0)
      print("working")
    if message == "Purple":
      red.set_PWM_dutycycle(RED_PIN, 100)      
      green.set_PWM_dutycycle(GREEN_PIN, 0)
      blue.set_PWM_dutycycle(BLUE_PIN, 100)

      print("working")
    
    if message.startswith("Send"):
      values= message.split()
      red.set_PWM_dutycycle(RED_PIN, int(values[1]))      
      green.set_PWM_dutycycle(GREEN_PIN, int(values[2]))
      blue.set_PWM_dutycycle(BLUE_PIN, int(values[3]))


  def on_close(self):
    print('[WS] Connection was closed.')


application = tornado.web.Application([
  (r'/', MainHandler),
  (r'/ws', WSHandler),
  ], **settings)


if __name__ == "__main__":
    try:
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(PORT)
        main_loop = tornado.ioloop.IOLoop.instance()
        print("Tornado Server started")
        main_loop.start()

    except:
        print("Exception triggered - Tornado Server stopped.")
        pigpio.cleanup()
        
