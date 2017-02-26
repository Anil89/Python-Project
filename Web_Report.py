 # -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 09:50:18 2017

@author: anil
"""
#import re

import sys
#import time


from bs4 import BeautifulSoup as bs
from lxml import html
import requests
def get_soup(url):
    try:
        session = requests.session()
        response = session.get("http://"+url)
        print(response.status_code)
        if response.status_code == 200:
            soup = bs(response.content, 'html.parser')
            return soup
        else:
            return None
    except Exception as error:
      e = sys.exc_info()[1]
      print ('Exception Raised : ' + (str(e)))
      return False
        
def get_data(row):
  prop_url = row
  soup = get_soup(prop_url)
  
  if soup:
    tree = html.fromstring(str(soup))
    values=[prop_url.strip()]
     
    val = ['sale','Sale','Cart','cart','Price','price','Best Deal','Buy','buy']
    state = []
    state = [tree.xpath('//*[contains(text(),"'+x+'")]/text()')  for x in  val]
    print(state)
    state = [x for x in state if x]
    status = True if state else False
    print(status)
  else:
    status = "False"

  fp = open('websites_report.txt','a')
  fp.write(prop_url+"\t"+str(status)+"\n")                                            # get data in text headers in
  fp.close() 


urls_file = "sites.txt"
t = open(urls_file,'r')
rows = t.readlines()
t.close()
col_headers = ['website','e-commerce']


fp = open('websites_report.txt','w')
fp.write('\t'.join(col_headers))
fp.close()

for row in rows[:]:
   try:
       get_data(row.strip())
   except Exception as error:
    print(error)
    e = sys.exc_info()[1]
    print ("'Exception Raised -----------' "+str(e))
