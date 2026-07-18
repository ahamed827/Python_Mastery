l=[3,2,4,5]
k=len(l)
lar=l[0]
seclar=l[0]
for i in range(k):
    if l[i]>lar:
        seclar=lar
        lar=l[i]
    elif l[i]>seclar and l[i]!=lar:
        seclar=l[i]
print(seclar)
        
