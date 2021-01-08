def myfunc(n):
    return abs(n - 50)
mylist = [100, 50, 65, 82, 23]
mylist.sort(key = myfunc)
print(mylist)