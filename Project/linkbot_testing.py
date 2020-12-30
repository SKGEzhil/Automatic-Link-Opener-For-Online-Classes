

# Import webbrowser and time module 
import webbrowser
import time 
  
# Input Site
link_1 = "https://skgezhil.blogspot.com"
link_2 = "https://facebook.com/skgezhil2005"
link_3 = "https://instagram.com/skgezhil2005"
link_4 = "https://youtube.com/skgezhil/"
link_5 = "http://google.com/search?q=skgezhil"

#Variables
link_count = 0

# Time for opening links
timer_1 = "17:50:10"
timer_2 = "17:50:15"
timer_3 = "17:50:20"
timer_4 = "17:50:25"
timer_5 = "17:50:30"

# This is the actual time
Current_time = time.strftime("%H:%M:%S") 

#Functions
def open_link_1():
  Current_time = time.strftime("%H:%M:%S")
  if(Current_time != timer_1) :
    while (Current_time != timer_1):
      print ("Waiting for test_timer_1")
      print ("Waiting, the current time is " + Current_time +" :-( " )
      Current_time = time.strftime("%H:%M:%S") 
      time.sleep(1)
  if(Current_time == timer_1):
    webbrowser.open(link_1)
    while (Current_time != timer_1):
      print ("Waiting for test_timer_1")
      print ("Waiting, the current time is " + Current_time +" :-( " )
      Current_time = time.strftime("%H:%M:%S") 
      time.sleep(1)
  if(Current_time == timer_1):
    open_link_2()

def open_link_2():
  Current_time = time.strftime("%H:%M:%S")
  if(Current_time != timer_2):
    while (Current_time != timer_2):
      print ("Waiting for timer_2")
      print ("Waiting, the current time is " + Current_time +" :-( " )
      Current_time = time.strftime("%H:%M:%S") 
      time.sleep(1)
  if(Current_time == timer_2):
    webbrowser.open(link_2)
    open_link_3()

def open_link_3():
  Current_time = time.strftime("%H:%M:%S")
  if(Current_time != timer_3):
    while (Current_time != timer_3):
      print ("Waiting for timer_3")
      print ("Waiting, the current time is " + Current_time +" :-( " )
      Current_time = time.strftime("%H:%M:%S") 
      time.sleep(1)
  if(Current_time == timer_3):
    webbrowser.open(link_3)
    open_link_4()

def open_link_4():
  Current_time = time.strftime("%H:%M:%S")
  if(Current_time != timer_4):
    while (Current_time != timer_4):
      print ("Waiting for timer_4")
      print ("Waiting, the current time is " + Current_time +" :-( " )
      Current_time = time.strftime("%H:%M:%S") 
      time.sleep(1)
  if(Current_time == timer_4):
    webbrowser.open(link_4)
    open_link_5()

def open_link_5():
  Current_time = time.strftime("%H:%M:%S")
  if(Current_time != timer_5):
    while (Current_time != timer_5):
      print ("Waiting for timer_5")
      print ("Waiting, the current time is " + Current_time +" :-( " )
      Current_time = time.strftime("%H:%M:%S") 
      time.sleep(1)
  if(Current_time == timer_5):
    webbrowser.open(link_5)
    open_link_1()

def opener_7():
  if(link_count == 0):
    open_link_1()

#Main

opener_7()