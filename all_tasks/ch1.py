import ast
import dis
def sqr(num):
    return num*num
def mult(a,b):
    return a*b
dis.dis(sqr)
dis.dis(mult)
# ----------------------
data=5
print(type(data))
data=[1,2,3]
print(type(data))
def my_func():pass
data=my_func
# ----------------------
my_list=[1,2,3,4]
print(id(my_list))
my_list.append(5)
print(id(my_list))
# is the same adress
# ------------------
code = "y = (4 * 5) - 3"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))