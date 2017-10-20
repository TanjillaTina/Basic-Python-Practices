# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 06:54:47 2017

@author: TINA
"""
# similar to try-catch block, but, here it can be used in alternate to if-else too
x=input("Enter a string ");
try: 
    x=int(x);
    print("Strin has converted to number ",x);
    print("After Addition ",(x+1));
except:
    print("Hey x ",x,"is a string");
    