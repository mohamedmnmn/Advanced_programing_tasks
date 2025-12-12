# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# mean_value = np.mean(arr)
# median_value = np.median(arr)
# std_value = np.std(arr)
# print("Mean:", mean_value)
# print("Median:", median_value)
# print("Standard Deviation:", std_value)
# # ------------------------------------------------
# import pandas as pd
# students = pd.DataFrame({
#     'Name': ['Ahmed', 'ali', 'omar', 'moamed', 'khalid'],
#     'Age': [20, 21, 19, 22, 20],
#     'Score': [85, 78, 92, 67, 88]})
# high_scorers = students[students['Score'] > 80]
# print(high_scorers)
# # ------------------------------------------------
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]
# plt.plot(x, y)
# plt.xlabel('X Values')
# plt.ylabel('Y Values')
# plt.title('Square Numbers')
# plt.show()
# ------------------------------------------------
# from flask import Flask
# app = Flask(__name__)
# @app.route('/hello')
# def hello():
#     return "Hello, Advanced Python!"
# if __name__ == '__main__':
#     app.run(debug=True)
# -------------------------------------------------
import torch
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])
dot_product = torch.dot(tensor1, tensor2)
elementwise_mul = tensor1 * tensor2
print("Dot Product:", dot_product)
print("Element-wise Multiplication:", elementwise_mul)