# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:02:36 2017

@author: TINA
"""

print("In The Name of Allah, The Beneficent and The Merciful");
# is and is not works similar to "==" and "!=" but, there is a difference
#in Python, "==" and "!=" considers only the value 
#where else "is" and "is not" considers value as well as the data type

######Examples
a=23.00;
b=23;
print("a= ",a,"b= ",b);
if a==b:
    print("Equal in type and value");
if a is b:
    print("Are equal in values but, not in data types");    
##########
intt=int(input("Enter an integer Number "));
flo=float(input("Enter Folating Point Number version of ur given integer number "));
if intt == flo:
    print("ur Enterd Numbers has same values");
    if intt is flo:
        print("Using is ur Enterd Numbers have different data types");
    else:
         print("but, numbers have different data types");
else:
    print("Numbers are different (values)");



##########
    
    

