#Strings Methods:
#(i)a.upper() (ii)a.lower() (iii)a.rstrip() (iv)a.lstrip() (v)a.replace (vi)a.strip() (vii)a.capitalize() (viii)a.title() (ix)a.center() (x)a.count("character") (xi)a.endswith("!!!") (xii)a.find('character') (xiii)a.index('character') (ix)a.isalnum() (x)a.isalpha (xi)a.isupper() (xii)a.islower() (xiii)a.isprintable() (xiv)a.isspace() (xv)a.istitle (xvi)a.startswith() (xvii)a.swapcase()
#Strings are immutable
a = "!!!Harry!!!!!! !!!Vishal!!!!!!"
b = 'jay shree ram'
c = 'Welcome to VS code'
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))#rstrip() removes heading '!'  (mtlab aage ka haata dega)
print(a.lstrip("!"))#lstrip() removes tale '!' (mtlab piche ka hata dega)
print(a.replace("Harry", "John"))#syntax: a.replace(old_name,new_name)a
print(a.split(" "))#split removes space between two words and make it as a list.
print(b.capitalize())# capitalize only 1st character of string and lower the rest of the characters if capital.
print(b.title())# capital only the 1st character of each letter in string  and lower the rest of the characters if capital
print(c.center(50,'.'))#syntax: x.center(width,fill_character)
print(a.count("!"))
print(a.endswith("!!!")) 
print(a.find("h"))#prints the index of 1st occurance of letter 'h' returns '-1' if there is no occurance of given character.
print(a.index("h"))#same as find but if there is no occurance of such characters then it returns value error.
str1 = "WelcomeToTheConsole"
print(str1.isalnum())#if there is space between the'wlecometoconsole' then it will return false else it is printing true(cuz only a-z A-Z and 0-9 only no spaces no special characters.)
print(str1.isalpha())
print(str1.isupper())  
print(str1.islower())
str2 = 'Demon Slayer Kimetsu No Yaiba \n'
print(str2.isprintable())#its returning false due to \n if there is no \n then it will print true.
str3 = "                   "
print(str3.isspace())#if there is only white space then it will print true otherwise false.
print(str2.istitle())#if 1st character of each letter is capital then it will return true otherwise false.
print(a.startswith("!!!"))#tale
str4 = "SWAPCASE SWAPS:)"
print(str4.swapcase())#changes upper to lower and vice versa

















