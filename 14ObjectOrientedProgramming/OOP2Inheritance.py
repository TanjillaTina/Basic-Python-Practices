# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 03:50:21 2017
In The Name of Allah, The Beneficent and The Merciful
@author: TINA
"""
class PartyAnimal:  ##Prent Class
   x = 0
   name = ""
   def __init__(self, nam):
     self.name = nam
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):  ##Inherited class
   points = 0
   def touchdown(self):
      self.points = self.points + 7
      self.party()
      print(self.name,"points",self.points)
      

#####End of defining class
s = PartyAnimal("tina")
s.party()

j = FootballFan("Sarkar")
j.party()
j.touchdown()
      
      
      
########### Another Example:
class Building:
      no_of_floors=0
      no_of_rooms=0
      def __init__(self, no_rooms,no_floors):
          self.no_of_floors =no_floors
          self.no_of_rooms =no_rooms
          print("Total no of floors ",self.no_of_floors,"Total no of rooms in each floor ",self.no_of_rooms)  
      def Comparee(self):
          if self.no_of_floors >= self.no_of_rooms :
              print("More Floors")
          else:
              print("More Rooms")
#####
class MyBuilding(Building): #inheritting Building
      Color=""
      def __init__(self, no_rooms,no_floors,colors):
          self.Color=colors
          self.no_of_floors= no_floors
          self.no_of_rooms=no_rooms
          Building(self.no_of_rooms,self.no_of_floors)
          
          
      
      def MyBuilColor(self):
          print("My Building's color is ",self.Color)
######


TO1=Building(3,4);
TO1.Comparee();
print("Printing MyBulding")
MyB=MyBuilding(5,1,"Ocean Blue")
MyB.Comparee();
MyB.MyBuilColor();