import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

student = pd.read_json("student-data.json")
subjects = ["Maths", "Science", "English", "SST", "Hindi", "IT"]

# for i in range(0, len(student["Student Name"])):
i=0


values = [student["Maths"][i], student["Science"][i], student["English"][i], student["SST"][i], student["Hindi"][i],
          student["IT"][i]]

fig, ax = plt.subplots(figsize=(6, 5), dpi=400)
plt.title("Marks Obtained", fontsize=16, fontweight="bold")
plt.xlabel("Name Of Subjects", fontweight="bold")
bar = plt.bar(subjects, values, color="#f5ad27")
plt.yticks([])

for p in bar:
    height = p.get_height()
    plt.text(x=p.get_x() + p.get_width() / 2, y=height + .90, s=format(height), ha='center')


fig

