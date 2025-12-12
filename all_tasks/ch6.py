import csv
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Grade"]) > 80:
            print(row["Name"])
# -----------------------------------------
import json
data = {"course": "Python", "duration": "3 months", "students": ["Ali", "Sara"]}
with open("course.json", "w") as f:
    json.dump(data, f)
with open("course.json", "r") as f:
    loaded_data = json.load(f)
print("Students:", loaded_data["students"])
# ------------------------------------------
import pandas as pd
data = {
    'ID': [1, 2, 3, 4],
    'Name': ['Ali', 'Sara', 'Omar', 'Mona'],
    'Salary': [50000, 60000, 55000, 65000]}
df = pd.DataFrame(data)
print(df)
df.to_excel('employees.xlsx')
df_read = pd.read_excel('employees.xlsx')
print(df_read[['Name', 'Salary']])
# --------------------------------------------
def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    json_data = {"people": data}
    with open(json_file, 'w') as f:
        json.dump(json_data, f)