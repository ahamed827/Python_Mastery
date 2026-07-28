# n=5
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
# else:
#     print("prime")

# n=2222
# original=n
# rev=0
# while n>0:
#     k=n%10
#     rev=(rev*10)+k
#     n=n//10
# print("Reversed Number {} ,Original Number {}".format(rev,original))
# if original!=rev:
#     print("it is not palindrome")
# else:
#     print("it is palindrome")

# n=[1,5,3,7]
# lar=n[0]
# for i in range(len(n)):
#     if n[i]>lar:
#         lar=n[i]
# print(lar)

# n=10
# a,b=0,1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b

# n=12345
# c=0
# temp=abs(n)
# if temp==0:
#     print(1)
# while temp>0:
#     temp//=10
#     c+=1
# print(c)

# n=111
# s=str(n)
# p=len(s)
# t=0
# temp=n
# while temp>0:
#     k=temp%10
#     t+=k**p
#     temp//=10
# if t==n:
#     print("Armstron number")
# else:
#     print("Not Armstrong number")

