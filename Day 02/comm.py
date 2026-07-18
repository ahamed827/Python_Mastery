l1=[2,3,4,6]
l2=[3,3,4,1]
l3=[]
# for i in range(len(l1)):
#     for j in range(len(l2)):
#         if l1[i]==l2[j]:
#             l3.append(l1[i])
# print(l3)
# l3=list(set(l1).intersection(set(l2)))
# print(l3)
s=set(l2)
for i in l1:
    if i in s:
        l3.append(i)
print(l3)