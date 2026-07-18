d1={'a':1,'b':2}
d2={'c':3,'d':4}
d3={}
for i in d1:
    d3[i]=d1[i]
for i in d2:
    d3[i]=d2[i]
print(d3)