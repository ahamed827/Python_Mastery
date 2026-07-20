def largest(num:list)->int:
    lar=num[0]
    for i in range(len(num)):
        if num[i]>lar:
            lar=num[i]
    return lar
l=[10,2,4,6,7]
print(largest(l))