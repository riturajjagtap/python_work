import random
import sys
import os

class Animal:
    _name=""
    _height=0
    _weight=0
    _sound=0

    def __init__(self,name,height,weight,sound):
        self._name=name
        self._height = height
        self._weight = weight
        self._sound = sound

    def setname(self,name):
        self._name=name

    def setheight(self,height):
        self._height=height

    def setweight(self,weight):
        self._weight=weight

    def setsound(self,sound):
        self._sound=sound

    def getname(self):
        return self._name

    def getheight(self):
        return self._height

    def getweight(self):
        return self._weight

    def getsound(self):
        return self._sound

    def getType(self):
        print("Animal")

    def tostring(self):
        return "{} is {} cm tall, {} kg and says {}".format(self._name,self._height,self._weight,self._sound)

cat=Animal("Whiskers", 33, 10, "Meow")
print(cat.tostring())

class Dog(Animal):
    __owner=""

    def __init__(self,name,height,weight,sound,owner):
        self.__owner=owner
        super(Dog,self).__init__(name,height,weight,sound)

    def setowner(self,owner):
        self.__owner=owner

    def getowner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def tostring(self):
        return "{} is {} cm tall, {} kg and says {} and is owned by {}".format(self._name,
                                                            self._height,
                                                            self._weight,
                                                            self._sound,
                                                            self.__owner)

spot=Dog("Spot", 50, 25, "Bow", "Joey")
print(spot.tostring())
