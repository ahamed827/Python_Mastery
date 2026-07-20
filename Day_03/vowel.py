# s="hamza"
# c=0
# for i in s:
#     if i=='a':
#         c+=1
#     elif i=='e':
#         c+=1
#     elif i=='i':
#         c+=1
#     elif i=='o':
#         c+=1
#     elif i=='u':
#         c+=1
# print(c)
def count_vowels(s):
    vowels="aeiouAEIOU"
    c=0
    for i in s:
        if i in vowels:
            c+=1
    return c
print(count_vowels("Hello World"))
