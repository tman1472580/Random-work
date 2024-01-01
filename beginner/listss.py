mylist = ["banana","cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

for i in mylist:
    print(i)

if "apple" in mylist:
    print("Yes")
else: 
    print("no")

mylist.insert(2, "Lychee")
print(mylist)

mylist.remove("Lychee")
print(mylist)

mylist.reverse()
print(mylist)
new_list = sorted(mylist)
mylist.sort()
print(new_list)
mylist3 = [1]*5

mylist4 = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5]

mylist5 = mylist.copy()
aa = [1,2,3,4,5,6]
b = [i*i for i in aa]

print(b)