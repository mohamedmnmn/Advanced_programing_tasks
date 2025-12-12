class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return self.width*2+self.height*2
rec1=rectangle(10,5)
print(rec1.perimeter())
print(rec1.area())
# ---------------------------------------
class employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    @classmethod
    def from_string(cls, employee_str):
        name, emp_id, salary = employee_str.split(",")
        return cls(name, emp_id, float(salary))
    def display_employee_info(self):
        print(f"name: {self.name} id:{self.employee_id} salary:{self.salary}")
emp1 = employee("John Doe", "E001", 60000)
emp1.display_employee_info()
emp2 = employee.from_string("Jane Smith,E123,50000")
emp2.display_employee_info()
# -----------------------------------------
class vehicle:
   def move(self):
       print('vehicle is moving') 
class car(vehicle):
    def move(self):
       print('car is moving') 
class bike(vehicle):
    def move(self):
       print('bike is moving') 
v=vehicle()
c=car()
b=bike()
l=[v,c,b]
for i in l:
    i.move()
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector3D(self.x + other.x,self.y + other.y,self.z + other.z)
    def __sub__(self, other):
        return Vector3D(self.x - other.x,self.y - other.y,self.z - other.z)
    def __mul__(self, other):
        return self.x * other.x +self.y * other.y +self.z * other.z
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
print( v1 + v2)        
print( v1 - v2)   
# ---------------------------------------------------
class shape:
    def area(self):
        return 0
class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return self.width*2+self.height*2
rec1=rectangle(10,5)
print(rec1.perimeter())
print(rec1.area())
def print_shape_area(shape):
    print(shape.area())
c = circle(10)
r = rectangle(4, 5)
print_shape_area(c)
print_shape_area(r)