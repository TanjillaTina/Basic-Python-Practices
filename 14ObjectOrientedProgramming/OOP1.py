# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 01:33:47 2017
In The Name of Allah, The Beneficent and The Merciful
@author: TINA
"""
###Start of defining class "PartyAnimal"
class PartyAnimal:
     x = 0

     def party(self) :
        self.x = self.x + 1
        print("So far",self.x)
###Start of defining class "PartyAnimal"
an = PartyAnimal() #ceating instance
an.party()
an.party()
an.party()
an2 = PartyAnimal() #ceating instances
an2.party()
#######


####Class: Constructors and Destructors
class PartyAnimal2:
      x = 0

      def __init__(self):
         print('PartyAnimal2 has been constructed')

      def party(self) :
         self.x = self.x + 1
         print('So far',self.x)

      def __del__(self):
          print('PartyAnimal2 has been destructed', self.x)

an3 = PartyAnimal2()
an3.party()
an3.party()
an3 = 42 #an3 is no linger objec, now it's integer 42
print('an3 contains',an3)

#####class with parameter :p (Constructor with parametres)

class PartyClass:
   x = 0
   name = ""
   def __init__(self, y):
     self.name = y
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

ob1 = PartyClass("Tina")
ob1 .party()

ob2 = PartyClass("Tanjilla")
ob2.party()
ob2.party()

##########



