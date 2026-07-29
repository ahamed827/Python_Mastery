k=[2,7,11,15]
t=9
l=0
r=len(k)-1
while l<r:
    cal=k[l]+k[r]
    if cal>t:
        r-=1
    elif cal<t:
        l+=1
    else:
        print(l,r)
        break

