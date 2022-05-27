# -*- coding: utf-8 -*-
pip install boto3
pip install awscli
pip install requests
pip install mysql
pip install mysql-connector-python-rf
pip install django
pip install selenium
pip install bitly-api

# Extract resources
import mysql.connector
curselist =[]
googlelist = []
tweetlist = []
joblist =[]

# create the connection object
myconn = mysql.connector.connect(host = server_ip_1 user = user_1, passwd = passwd1, 
                                 databese = database_1)
cur = myconn.cursor()
try:
    cur.execute ("select ID from category where live = 'live' order by prioty")
    result2 = cur.fetchall()
    for coursename in resul2:
        courselist.append(coursename[0])
        googlelist.append(coursename[1])
        tweetlist.append(coursename[2])
        joblist.append(coursename[3])
except:
myconn.rollback()
mycinn.close()
courselist
coursedic

import nltk
import string
import re

nltk.download ('punkt')
nltk.download('stopword')
from nltk.tokenizer import word_tokenize
from nltk.corpus import stopwords

course_with_tages = {}
for courseid, course in coursedict.item():
    course = course.lower ()
    words = word_tokenizer (course)
    word_without_punctuation = [w for w in words if w.lower() not in string.punctuation]
    lang_stopwords = stopwords.words('english')
    words_without_stopwords = [ w for w in word_without_punctuation if w.lowernot in lang_stop]
    
    for word in word_without_stopwords:
        if word in course_with_tags:
            word_courseid_list = course_with_tages[word]
            word_courseid_list.append (courseid)
            word_courseid_list = list (set (word_courseid_list))
        else:
            course_with_tags.update ({word:[courseid]})
del course_with_tages ["programming"]       
del course_with_tages ["design"]    
course_with_tags

def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    data = re.sub(clean, '', text)
    data = re.sub('&nbsb;',',data')
    return data

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import Expected_condition as Ec
drom selenium.webdriver.common.by import by
from selenium.common.exceptions import timeoutexception
import pandas as pd
from selenium,common.exceptions import StaleElementReferenceException
import requests

browser= webdriver.Chrome("my co mputer path")
browser.maximize_window()
jobdictionary ={}

indexcounter = 0
for jobid, jobname  in jobdict.item():
    keyword = Jobname
    location = 'Unites State'
    joblist =[]
    
    




































        