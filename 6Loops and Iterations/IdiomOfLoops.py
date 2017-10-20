# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 09:36:17 2017

@author: TINA
"""
print("In The Name of Allah, The Beneficent and The Merciful");
####### Find out the largest number
largest=None; #none is a special marker,it is considered as a constant in python and that saves a no value to the variable 
for i in [23,6,13,99,34,23]:
    if largest==None:  #we can also write it as, if larget is None:
        largest=i;
    elif i>largest:
      largest=i;
print("Largest Number is ",largest);  

#########Indexing the NUmbers in a loop
ind=1;
sum=0;
total_num=0;
for i in [23,6,13,99,34,23]:
    
       print("Index ",ind," Number ->",i);
       ind=ind+1;
       total_num=total_num+1;
       sum=sum+i;
print("End of Loop and Summation is ",sum," Average is ",(sum/total_num));

###### if a cvertain value exists in the given range number
val=23;
for i in [6,13,99,34,23,99]:
    if i==val:
        print(i," Exits here");
    else:
         print(i, "isn't the value");
print("Out of For Loop");

#######
         


########
