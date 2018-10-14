# -*- coding: utf-8 -*-
import datetime
today = datetime.date.today()
day = today.strftime("%A")
month = today.strftime("%B")
date = today.strftime("%d")
year = today.strftime("%Y")

print("Today is {}, {} {}, {}".format(day,month,date,year ))
