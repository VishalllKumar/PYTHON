marks = [3,5,6,"Harry",True,]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5])     #INDEX ERROR
print(marks[-3])   #it meand len(marks) - 3  = 5 - 3 = 2  #output: 6
if "Harry" in marks:
    print('Yes')
else:
    print('No')
if "rr" in "Harry":   # same thing applies for string as well!
    print("Yes")
else:
    print("No")
print(marks)
print(marks[1:-1])    #its mean marks[1:len(marks) - 1] means marks[1:5-1] hence marks[1:4] --> output : [5 ,6 ,'Harry']
print(marks[1:4:2])   # omits or jumps '1'
print(marks[0:4:3])   # omits or jumps '2'   [start:stop(n-1):step(n-1 jump)]


#LIST COMPREHENSION:
lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)

names = ["Milo","Sarah","Bruno","Anastasia","Rosa"]
filtre = [i for i in names if len(i)>4]
filtre = [i for i in names if len(i)>4]
print(filtre) 

names = ["Milo","Sarah","Bruno","Anastasia","Rosa"]
filtre = [names[i] for i in range(len(names)) if names[i][0] == 'B' ]
print(filtre)

LIST METHODS:
(i)l.append() (ii)l.sort(reverse=True) (iii)l.reverse() (iv)l.index(value) (v)l.count(value) (vi)l.copy(listname) (vii)l.insert(index,value) (viii)l.extend()
l = [11,45,1,2,4,6]
print(l)
l.append(7)
l.sort(reverse=True) #if we write reverse=True inside the sort(..) then it print the list in descending order. aur agar nhi likhoge to asscending me hoga
l.reverse() # it will just reverse print the list output:[6,4,2,1,45,11]
print(l)
print(l.index(1)) # will return the index where '1' is located firstly from left to right.  output : 2
print(l.count(1)) # will return the occurance of '1'. output = 1
LIST ALIASING:
m = l # iska mtlab hai ki m jo hai l ka reference le rha hai mtlab ye original list ko change kr skta hai agar m ko change krenge to autpmaticaly l bhi change hojayhega
m[0] = 0 # m of 0, '0' me badal jayega then l of 0 bhi change hojaeyga 0 me.
print(l) #output : [0,45,1,2,4,6]
Another method for copying:
(I)1st method (by slicing):
x = [10,20,30,40]
y = x[:]
y[1] = 777
print(x)  # output : [10,20,30,40]
print(y)  # output : [10,777,30,40]
(II)2end method (by copy methof (l.copy()))
m = l.copy() # if we use copy method then it will just copy the elements from l and do not change the element of l if we want to edit.
m[0] = 0
print(m)
l.insert(1,899)  # SYNTAX : l.insert(index,value)  isme 899 jo hai 1 pe ajayega aur baki sab aage shift hojayenge.
print(l)
m = [900,1000,1100]
l.extend(m)  #it will append in front of l . output : [11,899,45,1,2,4,6,900,1000,1100]
print(l)
m = [900 , 1000 , 1100]
k = l + m   #its concatinating of two list it will work as extend method means according to the login the m list is extend in front of l list.
print(k)



