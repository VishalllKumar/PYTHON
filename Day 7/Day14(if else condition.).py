#if else condition statement in python.


# example 1:
a = int(input("Enter Your Age: "))
print("Your Age is: ",a)
if (a>=18):
    print("you can drive")
else:
    print("you cannot drive")


#example 2:
applePrice = 210
budget = int(input("Enter Budget:"))
if (applePrice <= budget):
    print("Alexa, add 1 kg apples to the cart.")
else:
    print("Alexa,  do not add Apples to the cart.")


# example 3 :
num = int(input("Enter the value of num: "))
if (num<0):
    print("Number is negative.")
elif(num==0):
    print("Number is zero.")
else:
    print("Number is even.")
print("I am happy now :)")


#