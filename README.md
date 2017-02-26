# Python-Project

from bs4 import BeautifulSoup as bs
from lxml import html

-We have to install in any os packages like pip(old) 'pip3 install bs4' 
bs4 4r soup
-lxml for xpath (css selector)
'pip install lxml'

import requests 

-request for status,session

import sys

-sys for  os file operations

Defined function get_soup()

-To know status_code == 200,session

tree = html.fromstring(str(soup))
- Form lxml we converting soup to html format

val = ['sale','Sale','Cart','cart','Price','price','Best Deal','Buy','buy']
- Given search criteria with this key words 
state = [tree.xpath('//*[contains(text(),"'+x+'")]/text()')  for x in  val]
- given val key words in xpath wih for loop

state = [x for x in state if x]
-given list compration for loop

status = True if state else False
- if condition for True are False

open('websites_report.txt','a')
- file opening with 'a' append mode

fp.write(prop_url+"\t"+str(status)+"\n")   
- file writing with 'write'  mode

fp.close() 
 - closeing file  
 
for row in rows[:]:
- for loop read the rows in file

try: and Exception:
- for Exception errors handling

get_data(row.strip())
- function calling with fuction get_data and with argument row






