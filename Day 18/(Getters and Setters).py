#Getter:
# class Myclass:
#     def __init__(self,value):
#         self._value = value
#     def show(self):
#         print(f"Value is {self._value}")
#     @property
#     def ten_value(self):
#         return 10 * self._value
# obj = Myclass(10)
# print(obj.ten_value)
# obj.show()   


# Setter:
# class Myclass:
#     def __init__(self,value):
#         self._value = value
#     def show(self):
#         print(f"Value is {self._value}")
#     @property
#     def ten_value(self):
#         return 10 * self._value
#     @ten_value.setter     #setter.
#     def ten_value(self,new_value):
#         self._value = new_value/10
        
# obj = Myclass(10)
# obj.ten_value = 76
# print(obj.ten_value)
# obj.show()   
