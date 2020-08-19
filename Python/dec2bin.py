#!/bin/python3.8

n=int(input("Please enter decimal number: "))
given_dec=n
#jauna massīva array izveidošana
array=[]
while (n!=0):
    a=int(n%2)
# array.append komanda pievieno massīvam jaunu vērtību
    array.append(a)
    n=int(n/2)

string=""
# lai nolasītu massīvu array no gala izmanto [::-1]
for j in array[::-1]:
# string=string+str(j) mainīgais kurš pārraksta massīva vienības rindā
    string=string+str(j)

#gala rezultāta izprintēšana uz ekrāna
print("The binary number for %d is %s"%(given_dec, string))

