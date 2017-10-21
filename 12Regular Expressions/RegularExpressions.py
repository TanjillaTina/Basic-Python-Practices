# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 22:34:01 2017
##In The name of Allah,The Beneficent and The Merciful
@author: TINA
"""
import re  ##to use REs, u must import them

####findind a certain word in file using "re.search()" 
x=0
filee = open('filename.txt')
for line in filee:
    line = line.rstrip()
    if re.search('Number', line) :  #Number is the word that I want to search
        print(line)
        x+=1;
print("Total occurance",x);

#####Finding a line that starts with  certain word
for line in filee:
    line = line.rstrip()
    if re.search('^<input', line) :  #"<input" is the word that I want to search and "^" is to indicate I want to search lines taht begins with "<input" 
        print(line)
        x+=1;
print("Total occurance",x);

########Matching and Extractig Data
#findall() gonna give u a list of strings that matches

ti = "I am Tina,my Birth Date is day: 21 ,month: 01 ,now the Time is Fri Oct 20 22:34:01 2017 "
wor=re.findall('[0-9]+',ti) #find all the words that starts with digits
print(wor)

#######Findind Uppercase Letters
le= re.findall('[TIDFW]+',ti)  ##find all the letters from "TIDFO" and print those u found 
print(le)

#####Fine Tuning String Extraction
s='from: using the : character'  #extract the mail id and company name usin split 

t=re.findall('^f.+:', s)
print(t);

######Again, Finding the company and sender name problem in Regex Version

st="this mail is from tina@softtech.net date=20/10/2017"
smail=re.findall('\S+@\S+',st)
print(smail)

##finding the host name in Regex
host=re.findall('@([^ ]*)',st)
print(host)

#########Escape Character
p=list()
cookie="Yesterday I bought a cookie,the grocer was asking $.30 for it, I offered him $.20 and at last agreed to sell it for $.25"
p=re.findall('\$[0-9.]+',cookie) #finding a dollar sign followed by one or more digits or dots
print(p)

####End :) 







  

        





