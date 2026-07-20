def average(*args):
    if not args:
        return 0.0
    return sum(args)/len(args)
print(average(10,20))