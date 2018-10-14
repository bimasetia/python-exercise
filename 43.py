# -*- coding: utf-8 -*-
import datetime

today = datetime.datetime.now()
year = today.strftime("%Y")
user = input("How Old You Are?:")

print("You we're born in ",int(year) - int(user))
