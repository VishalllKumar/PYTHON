# SYNTAX:-

# def function_name(parameters,paramet....,...): |#...............................
      # logic /codes                              |# kitne bhi parameters
      # return                                    |# and argumensts laga skete hai
# functioncall(arguments,arg....,...)            |# according to question


def calGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)    
calGmean(7,8)


def isgreater(a,b):
    if (a>b):
        print("first no. is greater.")
    else:
        print("secound no. is greater.")
isgreater(5,10)


def islower(a,b):
    if (a<b):
        print("first no. is smaller .")
    else:
        print("secound no. is greater . ")
islower(1,5)


def average(a,b=8):#b=8 ko bolte hai default argument and a is required argument.
    print((a+b)/2)
average(4)




