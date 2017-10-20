# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:35:06 2017

@author: TINA
"""

print("In The Name of Allah, The Beneficent and The Merciful");

######Writing While Loops 
print("While Loop Demo");
n=5;
while n!=0:
    print("From the loop ->",n);
    n=n-1; #Python don't have n--,n++,so, I miss these :(
print("While Loop Ends Here");

########Infinite While Loop and Adding Breaks in the Loop
while True:
    x=int(input("Enter Number "));
    if x>5:
       print("Coming Out From the Infinite While Loop"); 
       break;
print("Here While ends with Break");       
##end of loop  

##finishing While with Continue
while True:
    x=int(input("Enter Number "));
    
    if x<5:
       continue; 
    elif x>5:
       print("Coming Out From the Infinite While Loop"); 
       break;
       
      
print("Here While ends with Break"); 

 
     
    
     

 


