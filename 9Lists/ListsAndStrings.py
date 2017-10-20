# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:32:44 2017

@author: TINA
"""

st="Tanjilla Sarkar Tina"
li=st.split(); ##Extracts the words of a string
print("Printing List");
for i in range(len(li)):
    print(li[i]);
######the split function even succeeds to delete a lot of spaces
st2="a      lots       of       spaces    " 
li2=st2.split();
print("Printing List");
for i in range(len(li2)):
    print(li2[i]);
    
######Tabs,newlines and other characers can be removed too using split function al u have to do is declare them first
st3="Tanjilla,Sarkar,Tina"
li3=st3.split(',');    #I M telling the split function to split it on the basis of ',' character
print("Printing List");
for i in range(len(li3)):
    print(li3[i]);
    
#####Again the mail example (The Double Split)
s="this mail is from tina@softtech.net date=20/10/2017"  #extract the mail id and company name usin split 
s1=s.split();
s2=s1[4].split('@');
print("Name ",s2[0]);
print("ORG ",s2[1]);   
    