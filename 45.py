#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 22:43:43 2018

@author: dedisetyadi
"""

#while True:
 #   user = input("Please add new password:")
    
   # if len(user) < 6:
        #print("Password not fine")
    #elif user.isupper():
        #print("Password not fine")
    #elif user.isdigit():
        #print("Password not fine")
   # else:
        #print("Password is fine!")
        #break
#LOOPING FOR USERNAME
while True:
    user = input("Enter Username:")
    with open("users.txt", "r") as file:
        data = file.read()
        
        if str(user) in data:
            print("Username Already Exists")
            continue
        else:
            print("Username Is Fine")
            break
    

#LOOPING FOR PASSWORD
while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)