# #Sets :
# s = {2 ,4 ,2 ,6}
# print(s)
#  # sets are immutable.
#  # sets do not contain duplicate items.

# info = {"Carla",19,False,5.9,19}   #(sets are unordered collection of data items)
# print(info)  #output : (since sets are unordered collection of data items so there ouput will be unorderd mtlab koio bhi index pe koi bhi items store hojayega and we cant access set by indexing)

# harry = set()  # for empty set we write set()
# print(type(harry))  #set type

# for i in info:
#     print(i)   # it will print unorderly items.
    

# Set operations:
# (i)s1.union(s2)  (ii)s1.update(s2)  (iii)cities.union(cities2)  (iv)cities.intersection_update(cities2)  (v)cities.symmetric_difference(cities2) (vi)cities.difference(cities2) (vii)cities.isdisjoint(cities2)  (viii)issuperset()  (ix)issubset()  (x)cities.add("value")  (xi)cities.update(cities2) (xii)cities.remove("value") (xiii)

# s1 = {1,2,5,6}
# s2 = {3,6,7}
# print(s1.union(s2))   #it will combine both sets.
# print(s1)  
# s1.update(s2)  #it will change the value of s1.
# print(s1)


# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities3 = cities.union(cities2)     #it will combine both sets and store it to another
# print(cities3)



# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities.intersection_update(cities2)   #it will just take the common items in set and update it at the same  time
# print(cities)



# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities3 = cities.symmetric_difference(cities2)   #it will just take the uncommon items in set.
# print(cities3)



# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities3 = cities.difference(cities2)    #it will take the itme thats given in set1 but not in set2.
# print(cities3)



# cities = {"Tokyo","Madrid","Berlin","Delhi","Seoul"}
# cities2 = {"Seoul","Kabul"}
# print(cities.issuperset(cities2))     # iska mtlab cities 2 ka sara element cities me hai ki nhi.
# cities3 = {"Tokyo","Madrid","Delhi"}
# print(cities.issuperset(cities3))     # iska mtlab cities3 ka sara element cities me hai ki nhi.


# #subset is ulta of superset
# cities = {"Tokyo","Madrid","Berlin","Delhi","Seoul"}
# cities2 = {"Seoul","Kabul"}
# print(cities2.issubset(cities))     # iska mtlab cities ka sara element cities2 me hai ki nhi.
# cities3 = {"Tokyo","Madrid","Delhi"}
# print(cities3.issubset(cities))     # iska mtlab cities ka sara element cities3 me hai ki nhi.



# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities.add("Meow")   #it will just add one more value hehe:)
# print(cities)


# #REMOVE()/DISCARD()
# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# # cities.remove("Tokyo2")     #it will through an error because there is no "Tokyo2" in set.
# cities.discard("Tokyo2")     #it will not through error . it will just eat 5 star and do nothing
# print(cities)



# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# items = cities.pop()   #pop the element from last but dont know the element since it's unordered pair.
# print(cities)
# print(items)
# cities.update(cities)
# print(cities)



# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# del cities
# print(cities)  #name error kyuki upar humne del use krke delte krdiya set ko



# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities.clear() #will clear all the element from the set and prints empty set 
# print(cities)


#membership operator:
# info = {"Carla",19,False,5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent")



