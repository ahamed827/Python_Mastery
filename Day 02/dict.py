s="banana"
char_count={}
for i in s:
    if i in char_count:
        char_count[i]+=1
    else:
        char_count[i]=1
for i in char_count:
    print(i+":"+str(char_count[i]))