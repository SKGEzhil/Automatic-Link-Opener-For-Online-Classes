# Import webbrowser and time module

import webbrowser
import time

# Input Site

link_1 = "https://us04web.zoom.us/j/5333081919?pwd=VEFBem5FSGtRRTdudWIwT2FjeStKZz09"  # Replace this with your link
link_2 = "https://us04web.zoom.us/j/71552529474?pwd=cnNsWC9yay9zNGZTTDVWZjNZVnlsdz09"  # Replace this with your link
link_3 = "https://us04web.zoom.us/j/4112093039?pwd=VTJ1VVVpVHk1d0dibXpUS3MwM3Y5dz09"  # Replace this with your link
link_4 = "https://us04web.zoom.us/j/4059959139?pwd=ai9vRWlWcTdXZlVLZWtSWnc4RjA4dz09"  # Replace this with your link
link_5 = "https://zoom.us/j/7518325707?pwd=Q20zWkp4VlFBNGVDSUMwMXR3OGc3UT09"  # Replace this with your link

# Variables

link_count = 0
Current_time = time.strftime("%H:%M:%S")

# Time for opening links

timer_1 = "09:29:30"  # Replace with your time
timer_2 = "10:19:30"  # Replace with your time
timer_3 = "11:09:30"  # Replace with your time
timer_4 = "11:59:30"  # Replace with your time
timer_5 = "13:29:30"  # Replace with your time


# Starting of the flow

def open_link_1():
    # Start the timer
    Current_time = time.strftime("%H:%M:%S")
    if Current_time < timer_1:
        while Current_time != timer_1:
            print("Wed Waiting for timer_1")
            print("Waiting, the current time is " + Current_time + " :-( ")
            Current_time = time.strftime("%H:%M:%S")
            time.sleep(1)

    # Refreshing timer after reboot
    if timer_1 < Current_time < timer_2:
        open_link_2()
    if timer_2 < Current_time < timer_3:
        open_link_3()
    if timer_3 < Current_time < timer_4:
        open_link_4()
    if timer_4 < Current_time < timer_5:
        open_link_5()

    # Opening the link    
    if Current_time == timer_1:
        webbrowser.open(link_1)
        open_link_2()


# Function to Open link 2
def open_link_2():
    Current_time = time.strftime("%H:%M:%S")
    if Current_time != timer_2:
        while Current_time != timer_2:
            print("Wed Waiting for timer_2")
            print("Waiting, the current time is " + Current_time + " :-( ")
            Current_time = time.strftime("%H:%M:%S")
            time.sleep(1)
    if Current_time == timer_2:
        webbrowser.open(link_2)
        open_link_3()


# Function to Open link 3
def open_link_3():
    Current_time = time.strftime("%H:%M:%S")
    if Current_time != timer_3:
        while Current_time != timer_3:
            print("Wed Waiting for timer_3")
            print("Waiting, the current time is " + Current_time + " :-( ")
            Current_time = time.strftime("%H:%M:%S")
            time.sleep(1)
    if Current_time == timer_3:
        webbrowser.open(link_3)
        open_link_4()


# Function to Open link 4
def open_link_4():
    Current_time = time.strftime("%H:%M:%S")
    if Current_time != timer_4:
        while Current_time != timer_4:
            print("Wed Waiting for timer_4")
            print("Waiting, the current time is " + Current_time + " :-( ")
            Current_time = time.strftime("%H:%M:%S")
            time.sleep(1)
    if Current_time == timer_4:
        webbrowser.open(link_4)
        open_link_5()


# Function to Open link 5
def open_link_5():
    Current_time = time.strftime("%H:%M:%S")
    if Current_time != timer_5:
        while Current_time != timer_5:
            print("Wed Waiting for timer_5")
            print("Waiting, the current time is " + Current_time + " :-( ")
            Current_time = time.strftime("%H:%M:%S")
            time.sleep(1)
    if Current_time == timer_5:
        webbrowser.open(link_5)
        from linkbot_thursday import open_link_1
        open_link_1()


def opener_2():
    if link_count == 0:
        open_link_1()


# Main

opener_2()
