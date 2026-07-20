def reverse(s):
    # return s[::-1]
    rev=''
    for i in s:
        rev=i+rev
    return rev
print(reverse("hamza"))