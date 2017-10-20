# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:34:55 2017

@author: TINA
"""

#####Tking input and saving it in a list

x=[]
for i in range(0,5,1):
    j=int(input("Enter number "))
    x.append(j);  #Saves values In the list

print("Printing Numbers")
for i in range (0,len(x),1):
     print(x[i]);     
##########If a number exixts in the list
if 3 in x:
    print("3 exists in the list");
else:
    print("3 doesn't exists in the list");     
    
######### Sorting Lists
x.sort();

print("Printing Numbers(After Sortin)")
for i in range (0,len(x),1):
     print(x[i]);   
     

#######