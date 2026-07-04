#DECORATORS IN PYTHON

# def greet(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx
# @greet
# def hello():
#     print("Hello world")
# hello()


def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)     
# *args lets a function take many values without knowing how many will come.(tuple)
# **kwargs lets a function take many named values using keys and values.(dictionary)
        print("Thanks for using this function")
    return mfx
@greet
def hello():
    print("Hello world")
@greet
def add(a,b):
    print(a+b)

hello()
add(1,2)




