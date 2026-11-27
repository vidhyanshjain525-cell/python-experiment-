
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
students = ["A", "B", "C", "D", "E"]
marks = [80, 70, 90, 60, 85]

plt.figure()
plt.bar(students, marks)
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()


data = [10, 20, 25, 30, 35, 40, 45, 50, 60]

plt.figure()
plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()
