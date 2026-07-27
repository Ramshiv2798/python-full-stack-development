'''
Matplotlib
-------------
matplotlib library is an python library that provides
functionality to charts, graphs, bar and data visualization

eg:
import matplotlib.pyplot as plt

x = [2026,2025,2024,2023,2022]
y = [120,150,135,95,70]

plt.bar(x,y, color='red', edgecolor='Black')
plt.title("Car sales")
plt.xlabel("Years")
plt.ylabel("Number of cars")
plt.show()

Eg:
import matplotlib.pyplot as plt
subjects_= ['Python','Java','c']
stu_ = [69,13,50]

plt.pie(stu_, labels=subjects_,colors=['red','Blue','orange'],autopct='%1.1f%%')
plt.legend(subjects_)
plt.title('courses')
plt.show()


import matplotlib.pyplot as plt
x = ['BMW','SWIFT','ToYOTO']
y = [120,150,135]

plt.scatter(x,y,color='red')
plt.title('cars sales')
plt.xlabel('Years')
plt.ylabel('Number of cars')
plt.show()

import matplotlib.pyplot as plt

y = [10,40,20,50]

plt.hist(y,bins=20)
plt.title('cars sales')
plt.xlabel('Years')
plt.ylabel('Number of cars')
plt.show()

import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C", "C++", "SQL"]
marks = [85, 78, 92, 74, 88]

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(subjects, marks, marker='o')
plt.title("Line Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.subplot(2, 2, 2)
plt.bar(subjects, marks)
plt.title("Bar Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.subplot(2, 2, 3)
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")

plt.subplot(2, 2, 4)
plt.scatter(subjects, marks)
plt.title("Scatter Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

y = [10,40,20,50]

plt.hist(y,bins=1000)
plt.title('cars sales')
plt.xlabel('Years')
plt.ylabel('Number of cars')
plt.show()
'''
