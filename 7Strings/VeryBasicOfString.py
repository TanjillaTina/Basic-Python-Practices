# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:55:59 2017

@author: TINA
"""

print("In The Name of Allah, The Beneficent and The Merciful");
st1="Tanjilla";
st2="Tina";
st=st1+" "+st2;
print(st);

l=len(st); # Getting the Length 
print(l);
    
increment=1;
start=0; #Strings index starts from 0
for i in range(start,l,increment):
  print(st[i]);
  
#####Anothr way here, letter indicates each character in string
  for letter in st:
      print(letter);
      
############# using while
k=0;
while k<len(st):
    letter=st[k];
    print(letter);
    k=k+1;
######## printing of a certain range
print(st[9:13]); #printing from range 9-13 (Tina)

#########  printing frm begining to end
print(st[:]); 

######
begining=0;ending=14;
print(st[begining:ending]);

########

     
      
