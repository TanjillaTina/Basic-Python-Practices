# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:39:59 2017
In The Name of Allah, The Beneficent and The Merciful
@author: TINA
"""
##JSON represets data as nested "lists" and "Dictinaries"
import json

data = '''
{
  "name" : "Tanjilla Sarkar",
  "phone" : {
    "type" : "intl",
    "number" : "+0000000"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Number:', info["phone"])
print('Hide:', info["email"]["hide"])

#######Another Complex one

import json

data = '''
[
  { "id" : "14",
    "x" : "1",
    "name" : "Tina"
  } ,
  { "id" : "23",
    "x" : "2",
    "name" : "Sarkar"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

############
