# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:03:47 2017
##In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""

#Tuples are too much like lists

names=("Tanjilla","Sarkar","Tina") #context Syntax for a tuple
for i in names:
    print(i);


print(names[2]); #similar to lists

#######Almost similar built-in functions
a=(3,4,5,6,7,2)
print("Max Value",max(a)," Sum ",sum(a)) #and so on...but, not "sort"

#######Differences between list a tuple
#1,U can't alter the elements of a tuple, once an assignment is made, it's no modifiable just as the letter in string

#2.once u define the total number of items in a tuple, u can't add an extra element
#3. U needn't to use tuples instead of lists ( :p )


##Tuples cam be used to add two assignment statements

(Tina,Sarkar)=(3,2) ##tina=3,sarkar=2
print(Tina)
print(Sarkar)

######More examples in tuples, this is how we actualy use tuples in our code
di=dict() ##
di={'tina':1,'tina1':11,'tina11':111,'tina12':12,'tina121':121,'tina21':21}
for (k,v) in di.items():
    print(k,v)
    
####another
tups=di.items();
print(tups);

####Most efficient one
#Tuples can be comparable
if (0,1,2) > (2,5,4):  
    print("Bigger")
else:
    print("Not Bigger")
    
#####Sorting Lists of Tuple
##We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
for (k,v) in sorted(di.items()):  ##it sorts the dic by keys
    print(k,v)


