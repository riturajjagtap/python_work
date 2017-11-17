import random
import sys
import os

str="i will learn python in one month"
str2="  aa bbb cccc  "
print(str)
print(str.capitalize())
print(str2.isalpha())
print(len(str))
#print(str.replace("month","week"))

str=str.replace("month","week")
print(str)
print(str2.strip())

fp=open("test.txt","wb")
print(fp.name)
print(fp.mode)
fp.write(bytes("Testing","UTF-8"))
fp.close()


fp=open("test.txt","r+")
print(fp.read())
fp.close()

os.remove("test.txt")

