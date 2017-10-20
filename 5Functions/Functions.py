# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 07:18:05 2017

@author: TINA
"""

##In python the keywor def: starts definining a funtion it, also follows the identication as the conditional statements

def ToPrint():
    print("Hello I m printing from function");
#as the identation ends the function definition ends too
ToPrint(); # calling the defined function

#################
#examples of built-in funtions min and max
big=max("Hellow World");
print(big);
sml=min("Hellowworld");
print(sml);

##########
#defining functions eith arguments
def OddOrEven(a):
    if a%2==0:
        print("a is=",a," and it's even");
    else:     
        print("a is=",a," and it's odd");
##defining fubction ends here

for i in range(10): # here i starts from 0 and goes to 10
  OddOrEven(i); 
###calling again
x=int(input("Enter a number")); #takes inputs as integer

OddOrEven(x);

##########Defining Functins taht returns a value
def IReturn(a):
     if a%2==0:
        return "even";
     else:     
        return "odd";
#end of defining fubction 

for i in range(10): # here i starts from 0 and goes to 10
  print("Number",i,"is ->> ",IReturn(i));

##############
#Functions with Multple Parametres
def MultiP(OpName,a,b):
    if OpName=="Add":
        return (a+b);
    elif OpName=="Sub":
        return (a-b);
#end of defining function
print(MultiP("Add",4,3));
print(MultiP("Sub",10,6));

#############

    
    
    

      