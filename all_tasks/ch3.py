# def remove_vowels(str):
#     vowels=['a','e','i','o','u','y']
#     new_str=''
#     for s in str:
#         if s not in vowels:
#             new_str+=(s)
#     return new_str
# print(remove_vowels('abcdefg'))
# # -----------------
# l=[1,2,3,4,5]
# new_l=list(map(lambda x:x**2,filter(lambda x:x%2==1,l)))
# print(new_l)
# # --------------------------------
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(6))
# --------------------------
# def make_adder(n):
#     def adder(x):
#         return n + x
#     return adder
# x=make_adder(1)
# print(x(2))
# ------------------
# def apply_twice(func,v):
#     return func(func(v))
# print(apply_twice(lambda x:x+1,5))
# --------------------------
l=[1,2,3,4,5,6,7,8,9,10]
def reduce(func, li):
    result = li[0] 
    for item in li[1:]:
        result = func(result, item)
    return result
print(reduce(lambda x,y:x+y,l))