# FOR LOOP:
# example 1:
for i in range(5):
    print(i)
i = 0

# WHILE LOOP:
# example 1:
while (i<3):
    print(i)
    i = i + 1

# example 2:
i = 0
while i <= 34 :
    i = int(input("Enter number:"))
    print(i)

# example 3:
count = 10
while ( count > 0 ):
    print(count)
    count -= 1
else:# if while coditino not satisfied it automaticaly comes to the else part and print meow.
    print("meow")

# BREAK:
for i in range(1,12):
    if (i == 11):
        break      # it will break when i == 11 and terminates the loop
    print("5 x",i,"=",5*i)

# CONTINUE:
for i in range(1,12):
    if (i == 10):
        continue   # it will skip the i == 10 part and continue the loop
    print("5 x",i,"=",5*i)

# PASS:
for i in range(1,12):
    if(i==10):
        pass   # will do nothing:)
    print("5 x",i,"=",5*i)

# Nested Loops:=









