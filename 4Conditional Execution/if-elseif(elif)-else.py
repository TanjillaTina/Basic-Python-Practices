# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:08:26 2017

@author: TINA
"""

#Chained Conditions if-elseif(elif)-else
   #a=input("enter a integer");
   a=int(input("Enter integer number: "));
    #a=int(a);
    if a%3==0:
        print("a is dividible by 3");
    elif a%2==0:
        print("a is divisible by 2");
        
    else:
        print("None of them is true for a");
