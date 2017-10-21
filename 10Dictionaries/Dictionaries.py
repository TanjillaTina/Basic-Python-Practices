# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 20:00:17 2017
##In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""

#Similar to Maps in Java
bag=dict()  
bag['mirror']=1; #bag is dictionarie,mirror is index,1 is the value
bag['books']=2;
bag['pen']=4;
bag['chocolate']=3;
print(bag);
print(bag['books']);


##Updating value
bag['chocolate']=bag['chocolate']+33;
print(bag['chocolate']);
#########

######Comparing Lists and Dictionaries

li=list()
li.append(14)
li.append(23)
print("Printin List ",li)
#Updating value
li[1]=22
print(li)


#########Simple Assigning the values

ti1=dict() ##It can be also done by this statement: ti1={}
ti1={'tina':1,'tina1':11,'tina11':111,'tina12':12,'tina121':121,'tina21':21}
print(ti1);

#########


#######Dictionarie Literals

###We can use the in operator to see if a key is in the dictionary
##This program demostarte the creation of histogram(counting the frequecies)
counts = dict()
names = ['tina', 'tanjilla', 'tina', 'tina', 'tanjilla','tanjilla','Sarkar']
for name in names :
    if name not in counts: 
       counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)


#######if a key exixts in the Dic
if 'tina' in counts:
    print("Tina exists in dic");
else:
    print("Tina dosen't exist in dic");
#####The get method for dictionaries

ti = counts.get('tanjilla', 0)
print(ti)



########### Ceating histogram reading a line
hist=dict()
#line=input("Enter the line plz ");
line="But soft what light through yonder window breaks It is the east and Juliet is the sun Arise fair sun and kill the envious moon Who is already sick and pale with grief"
words=line.split();
for word in words:
    if word in hist:
        hist[word]+=1
    else:
        hist[word]=1
print("Here Count ends")
print(hist)

#####The onus, we can use two iteration variables at a time in pyton(without creating an extra loop)
print("Printing from Histogram again "); 
for keys,values in hist.items():
    print("Key-->>",keys," Value-->>",values)
    
######





