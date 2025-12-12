products = ["  LAPTOP ", "phone  ", "  Tablet", "CAMERA  "]
str = list(map(lambda x: x.strip().title(), products))
print(str)
# -------------------------------------------
celsius = [0, 10, 20, 30, 40]
fa = list(map(lambda x: (9/5)*x + 32, celsius))
print(fa)
# -------------------------------------------
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x*x + 10, nums))
print(result)
# --------------------------------------------
words = ["python", "lambda", "programming", "map", "function"]
pairs = list(map(lambda x: (x[0], x[-1]), words))
print(pairs)
# ---------------------------------------------
marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]
updated = list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks))
print(updated)
#----------------------------------------------- 
nums = [5, 10, 15, 20, 25]
mn = min(nums)
mx = max(nums)
normalized = list(map(lambda x: (x - mn) / (mx - mn), nums))
print(normalized)
# ----------------------------------------------
str = [
    "my nam is mohamed",
    "i love python",
    "i love programming"]
lengths = list(map(lambda s: list(map(len, s.split())), str))
print(lengths)

