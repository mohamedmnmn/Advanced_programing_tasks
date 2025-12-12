# class Vector3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __add__(self, other):
#         return Vector3D(self.x + other.x,self.y + other.y,self.z + other.z)
#     def __sub__(self, other):
#         return Vector3D(self.x - other.x,self.y - other.y,self.z - other.z)
#     def __mul__(self, other):
#         return self.x * other.x +self.y * other.y +self.z * other.z
#     def __repr__(self):
#         return f"Vector3D({self.x}, {self.y}, {self.z})"
# v1 = Vector3D(1, 2, 3)
# v2 = Vector3D(4, 5, 6)
# print( v1 + v2)        
# print( v1 - v2)     
# ---------------------------------------------
# class Positive:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#     def __get__(self, obj, objtype=None):
#         return getattr(obj, self.name)
#     def __set__(self, obj, value):
#         if value < 0:
#             raise ValueError
#         setattr(obj, self.name, value)
# class BankAccount:
#     balance = Positive()
#     def __init__(self, start_balance=0):
#         self.balance = start_balance 
# acc = BankAccount(100)
# print(acc.balance)  
# acc.balance = -50
# print(acc.balance)#value error
# -------------------------------------------
# class Point:
#     __slots__ = ("x", "y")
# p = Point()
# p.x=1
# p.y=2
# p.z=3#AttributeError
# ------------------------------------------
import dis
def clculate_sum(a,b):
    return a+b
dis.dis(clculate_sum)