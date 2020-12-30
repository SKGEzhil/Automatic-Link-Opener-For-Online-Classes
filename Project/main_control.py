import time 
import datetime
from datetime import datetime

#Variables
day = datetime.today().weekday()
monday = 0
tuesday = 1
wednesday = 2
thursday = 3
friday = 4
saturday = 5
sunday = 6

#Operator
if(day == monday):
    from linkbot_monday import *
    open_link_1()
if(day == tuesday):
    from linkbot_tuesday import *
    open_link_1()
if(day == wednesday):
    from linkbot_wednesday import *
    open_link_1()
if(day == thursday):
    from linkbot_thursday import *
    open_link_1()
if(day == friday):
    from linkbot_friday import *
    open_link_1()
if(day == saturday):
    from linkbot_saturday import *
    open_link_1()
if(day == sunday):
    from linkbot_testing import *
    open_link_1()