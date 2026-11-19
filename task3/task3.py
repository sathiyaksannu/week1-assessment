
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Task 1: NumPy Operations

# Create marks array (4 students x 3 subjects)
marks = np.array([
    [78, 85, 90],
    [88, 76, 95],
    [92, 89, 84],
    [65, 70, 75]
])

print("Original Marks:")
print(marks)

# Print array shape
print("\nShape:", marks.shape)

# Student averages (axis=1)
student_avg = np.mean(marks, axis=1)
print("\nStudent Averages:", student_avg)

# Subject averages (axis=0)
subject_avg = np.mean(marks, axis=0)
print("\nSubject Averages:", subject_avg)

# Add 5 grace marks using broadcasting
grace_marks = marks + 5
print("\nMarks after adding 5 grace marks:")
print(grace_marks)

# Calculate weighted scores using np.dot()
weights = np.array([0.4, 0.3, 0.3])

weighted_scores = np.dot(grace_marks, weights)

print("\nWeighted Scores:", weighted_scores)


# Task 2: Pandas Operations

# Load employees.csv
employees = pd.read_csv("data/employees.csv")

print("\nEmployee Data:")
print(employees)

# Display dataset information
print("\nDataset Information:")
employees.info()

# Display statistical summary
print("\nStatistical Summary:")
print(employees.describe())

# Display selected rows and columns using loc
print("\nUsing loc:")
print(employees.loc[0:2, ["name", "department"]])

# Display selected rows and columns using iloc
print("\nUsing iloc:")
print(employees.iloc[0:3, 0:3])

# Filter employees based on salary
print("\nEmployees with salary greater than 30000:")
print(employees[employees["salary"] > 30000])


# Task 3: Data Cleaning

# Introduce 2 missing salaries
employees.loc[0, "salary"] = np.nan
employees.loc[2, "salary"] = np.nan

# Add 1 duplicate row
employees = pd.concat([employees, employees.iloc[[0]]], ignore_index=True)

print("\nEmployee Data with Missing Salaries and Duplicate:")
print(employees)


# Fill missing salaries using median
median_salary = employees["salary"].median()

employees["salary"] = employees["salary"].fillna(median_salary)

print("\nMedian Salary:", median_salary)

# Remove duplicate rows
employees = employees.drop_duplicates()

# Correct data types
employees["id"] = employees["id"].astype(int)
employees["salary"] = employees["salary"].astype(int)

print("\nCleaned Employee Data:")
print(employees)

# Check final dataset information
print("\nCleaned Dataset Information:")
employees.info()


# Task 4: GroupBy and Aggregation

# Group employees by department
department_summary = employees.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

print("\nDepartment Summary:")
print(department_summary)

# Load departments.csv
departments = pd.read_csv("data/departments.csv")

print("\nDepartment Data:")
print(departments)

# Display headcount for each department
print("\nHeadcount:")
for department in ["Sales", "HR", "IT", "Finance"]:
    count = department_summary.loc[department, "headcount"]
    print(f"{department}: {count}", end=" | ")
print()

# Inner Join
inner_join = pd.merge(
    employees, departments, on="department", how="inner"
)

print("\nInner Join:")
print(inner_join)

# Left Join
left_join = pd.merge(
    employees, departments, on="department", how="left"
)

print("\nLeft Join:")
print(left_join)

# Outer Join
outer_join = pd.merge(
    departments, employees, on="department",
    how="outer", indicator=True
)

print("\nOuter Join:")
print(outer_join)

# Find departments without employees
empty_departments = outer_join.loc[
    outer_join["_merge"] == "left_only", "department"
]

print("\nDepartments with no employees:")
print(empty_departments.tolist())

# Task 5: Matplotlib Charts

# Bar Chart - Average Salary by Department

avg_salary = employees.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
plt.bar(avg_salary.index, avg_salary.values, label="Average Salary")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()

plt.savefig("charts/bar_chart.png")
plt.show()

print("\nInsight: Finance department has the highest average salary.")

# Histogram - Employee Salary Distribution

plt.figure(figsize=(8, 5))
plt.hist(employees["salary"], bins=5, label="Employee Salaries")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()

plt.savefig("charts/histogram.png")
plt.show()

print("\nInsight: The histogram shows how employee salaries are distributed.")

# Scatter Plot - Salary vs Employee ID

plt.figure(figsize=(8, 5))
plt.scatter(employees["id"], employees["salary"], label="Employees")

plt.title("Employee Salary vs Employee ID")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()

plt.savefig("charts/scatter_plot.png")
plt.show()

print("\nInsight: The scatter plot shows the salary of each employee.")

# Line Chart - Employee Salary Trend

plt.figure(figsize=(8, 5))
plt.plot(employees["id"], employees["salary"], marker="o", label="Salary Trend")

plt.title("Employee Salary Trend")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()

plt.savefig("charts/line_chart.png")
plt.show()

print("\nInsight: The line chart shows how salaries vary across employees.")


