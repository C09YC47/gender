#!/usr/bin/env python

"""
Author: Akshay Ravi
Date: June 2019
Title: get Gender by name

enter a name and get its gender
diana = female
william = Male

"""
import json
from urllib.request import urlopen
user_input = input()
def getGender():
    global user_input
    get = urlopen("https://gender-api.com/get?&key=LDdMjsYsxGkKtzRQbn&name="+user_input).read()
    jSon = json.loads(get)
    print("Name :",user_input)
    print("Gender :",jSon.get("gender"))
    print("Country :",jSon.get("country"))
    print("program created by Akshay Ravi(C09Y C47)")
try:
    getGender()
except:
    print("try again")
"""'finally:
    print("This code might not work for you'")"""