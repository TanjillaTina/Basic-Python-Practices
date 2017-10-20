# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:00:58 2017

@author: TINA
"""


print("In The Name of Allah, The Beneficent and The Merciful");
#in python lists can save various typs of data,and alist can contain another list
names=["Tanjilla","Sarkar","Tina"]
for i in names:
    print(i);


print(names[2]);

#####Sorting Lists same as array

a=[3,4,5,6,7,2]
l=len(a);
for i in range(0,l-1,1):
    for j in range(0,l-i-1,1):
        if a[j]>a[j+1]:
            temp=a[j];
            a[j]=a[j+1];
            a[j+1]=temp;

print("Sorting is done and after sorting");
for i in range(0,l,1):
    print(a[i]);

#######Using the range
print(range(4));
print(range(len(names)));

######### Printing Using range-len
print("Printing Using Len-Range");
for i in range(len(a)):
    print(a[i]);

########Concatenating Lists Using +
print("After Concatenation");    
ti=names+a;
for i in range(len(ti)):
    print(ti[i]);
    
######Just Like Strings,Lists can be Sliced
    
print(names[:]);
print(a[3:6]) #it's from 3 to 5,not including index number 6
print(a[:6])
    








    

                