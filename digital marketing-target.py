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
    for name in resul2:
        list.append(cname[0])
        googlelist.append(name[1])
        tweetlist.append(name[2])
        joblist.append(name[3])
except:
myconn.rollback()
mycinn.close()
list
dic

import nltk
import string
import re

nltk.download ('punkt')
nltk.download('stopword')
from nltk.tokenizer import word_tokenize
from nltk.corpus import stopwords

c_with_tages = {}
for cid, c in cdict.item():
    c = c.lower ()
    words = word_tokenizer (c)
    word_without_punctuation = [w for w in words if w.lower() not in string.punctuation]
    lang_stopwords = stopwords.words('english')
    words_without_stopwords = [ w for w in word_without_punctuation if w.lowernot in lang_stop]
    
    for word in word_without_stopwords:
        if word in c_with_tags:
            word_cid_list = c_with_tages[word]
            word_cid_list.append (cid)
            word_cid_list = list (set (word_cid_list))
        else:
            c_with_tags.update ({word:[cid]})
del c_with_tages ["programming"]       
del c_with_tages ["design"]    
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
    
    




































        
