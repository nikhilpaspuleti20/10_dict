"""
DATE:29th NOV 2022
DAY:tuesday
TOPIC:dictionary
AUTHOR:nikhil
"""
foods={1:'magic',2:'pasta',3:'panipuri',4:'fied rice'}
print (foods[2])#'pasta' 
#print(foods[5])
h={}
print(type(h))#dict
f={1:'good',2:'bad',3:7,4:6.2,5:[1,4],6:(4,3)}
print(f.keys())#1,2,3,4,5,6
print(f.values())
print(f.items())
f.clear()
print(f)
b=[10,20,30,40,50,60]
print(dict.fromkeys(b,25))#{10:25,20:25,30:25,40:25,50:25,60:25}
c={1:"",2:"nikhil",3:7,4:5.2}
print(c.get(3))
print(c.get(2))
c.pop(4)
print(c)
c.popitem()
print(c)
k={1:"",2:"nikhil",3:5,4:3.2}
k.update({3:"varoon"})
print(k)
l={1:"hari",2:"nikhil",3:5,4:5.2}
l.setdefault(4,"nikhil")
print(l)
l.setdefault(5,"varoon")
print(l)