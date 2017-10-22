# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:10:12 2017
In The Name of Allah, The Beneficent and The Merciful
@author: TINA
"""
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))


