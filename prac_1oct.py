#1. Create a dictionary containing the following information for 5 students print("Hello")

import pandas as pd
print("Pandas imported successfully")
data = {
    "Student ID": [1, 2, 3, 4, 5],
    "Student Name": ["A", "B", "C", "D", "E"],
    "Python Marks": [80, 70, 90, 60, 85],
    "DBMS Marks": [75, 80, 85, 65, 90],
    "Mathematics Marks": [85, 75, 80, 70, 95]
}
print("Dictionary created")
df = pd.DataFrame(data)
print("DataFrame created")
print(df)


#2.Convert it into a Pandas DataFrame
import pandas as pd
data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Employee_Name': ['MK', 'JK', 'RM', 'JM', 'V'],
    'Department': ['CSE', 'IT', 'HR', 'CSE', 'Finance'],
    'Salary': [45000, 60000, 55000, 75000, 40000],
    'Experience': [2, 5, 4, 8, 3]
}
df = pd.DataFrame(data)
print("Employee Data:")
print(df)
print("\nEmployees with salary greater than 50000:")
print(df[df['Salary'] > 50000])
print("\nAverage Salary:", df['Salary'].mean())
print("Highest Salary:", df['Salary'].max())
print("\nEmployee with Highest Experience:")
print(df.loc[df['Experience'].idxmax()])


#3.Then find the product having the highest total sales.
import pandas as pd
data = {
    'Product_ID': [1, 2, 3, 4, 5],
    'Product_Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Printer'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics'],
    'Price': [50000, 500, 1500, 12000, 8000],
    'Quantity': [2, 10, 5, 3, 4]
}
df = pd.DataFrame(data)
df['Total_Amount'] = df['Price'] * df['Quantity']
print("Product Data:")
print(df)
print("\nProduct with Highest Total Sales:")
print(df.loc[df['Total_Amount'].idxmax()])


#4.Convert the dictionary into a DataFrame(patient)
import pandas as pd
data = {
    'Patient_ID': [101, 102, 103, 104, 105],
    'Patient_Name': ['MK', 'JK', 'RM', 'JM', 'V'],
    'Age': [65, 35, 72, 55, 68],
    'Disease': ['Diabetes', 'Fever', 'Heart Disease', 'Asthma', 'Diabetes'],
    'Medical_Charges': [60000, 15000, 85000, 30000, 55000]
}
df = pd.DataFrame(data)
print("Patients above 60 years:")
print(df[df['Age'] > 60])
print("\nAverage Medical Charge:", df['Medical_Charges'].mean())
print("Maximum Medical Charge:", df['Medical_Charges'].max())
print("\nPatients with charges greater than 50000:")
print(df[df['Medical_Charges'] > 50000])


#5.Create a DataFrame and calculate:
import pandas as pd
data = {
    'Order_ID': [101, 102, 103, 104, 105],
    'Customer': ['MK', 'JK', 'RM', 'JM', 'V'],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Printer'],
    'Quantity': [1, 2, 1, 2, 3],
    'Price': [60000, 20000, 25000, 10000, 5000],
    'Discount': [5000, 2000, 1000, 500, 1000]
}
df = pd.DataFrame(data)
df['Final_Amount'] = df['Quantity'] * df['Price'] - df['Discount']
print("All Orders:")
print(df)
print("\nOrders above 5000:")
print(df[df['Final_Amount'] > 5000])
print("\nHighest Value Order:")
print(df.loc[df['Final_Amount'].idxmax()])
print("\nAverage Order Value:", df['Final_Amount'].mean())


#6.Create a DataFrame and calculate:
import pandas as pd
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['MK', 'JK', 'RM', 'JM', 'V'],
    'Department': ['CSE', 'IT', 'CSE', 'ENTC', 'IT'],
    'Total_Classes': [100, 90, 80, 100, 120],
    'Classes_Attended': [65, 80, 55, 90, 85]
}
df = pd.DataFrame(data)
df['Attendance_Percentage'] = (
    df['Classes_Attended'] / df['Total_Classes']
) * 100
print("Student Attendance:")
print(df)
print("\nStudents with attendance below 75%:")
print(df[df['Attendance_Percentage'] < 75])


#7.A retail shop maintains sales information in a Python dictionary containing Product_ID, Product_Name, Category, Price, and Quantity.
import pandas as pd
data = {
    'Product_ID': [1, 2, 3, 4, 5],
    'Product_Name': ['Laptop', 'Mobile', 'Mouse', 'TV', 'Keyboard'],
    'Category': ['Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories'],
    'Price': [45000, 15000, 500, 30000, 1200],
    'Quantity': [2, 3, 10, 1, 8]
}
df = pd.DataFrame(data)
df['Total_Sales'] = df['Price'] * df['Quantity']
print("Product Data:")
print(df)
print("\nProducts with sales greater than 10000:")
print(df[df['Total_Sales'] > 10000])
print("\nProduct with Maximum Sales:")
print(df.loc[df['Total_Sales'].idxmax()])
print("\nAverage Sales:", df['Total_Sales'].mean())


#8.7. Create a Pandas Series using a dictionary where the student names are keys and their marks are values.
import pandas as pd

marks = {
    'MK': 80,
    'JK': 92,
    'RM': 65,
    'V': 88,
    'JM': 72
}
s = pd.Series(marks)
print("Student Marks:")
print(s)
print("\nMarks of Priya:", s['Priya'])
print("Maximum Marks:", s.max())
print("Minimum Marks:", s.min())
print("Average Marks:", s.mean())
print("\nStudents scoring more than 75:")
print(s[s > 75])


#9.8.	Create a Pandas Series using a dictionary containing employee names and their salaries.
import pandas as pd
salary = {
    'MK': 45000,
    'JK': 65000,
    'RM': 55000,
    'V': 80000,
    'JM': 40000
}
s = pd.Series(salary)
print("Employee Salaries:")
print(s)
print("\nHighest Salary:", s.max())
print("Lowest Salary:", s.min())
print("Average Salary:", s.mean())
print("\nEmployees earning more than 50000:")
print(s[s > 50000])

#10.9.	Create a Pandas Series using a dictionary containing product names and prices.
import pandas as pd
prices = {
    'Laptop': 50000,
    'Mouse': 800,
    'Keyboard': 1500,
    'Monitor': 12000,
    'Printer': 9000
}
s = pd.Series(prices)
print("Product Prices:")
print(s)
s = s * 1.10
print("\nPrices after 10% Increase:")
print(s)
print("\nMost Expensive Product:")
print(s.idxmax(), ":", s.max())
print("\nProducts costing more than 1000:")
print(s[s > 1000])


#11.10.	Create a Pandas Series using a dictionary where patient IDs are the index and patient ages are the values.
import pandas as pd
ages = {
    101: 45,
    102: 67,
    103: 32,
    104: 81,
    105: 59
}
s = pd.Series(ages)
print("Patient Ages:")
print(s)
print("\nAverage Age:", s.mean())
print("Oldest Patient:", s.idxmax(), "Age:", s.max())
print("Youngest Patient:", s.idxmin(), "Age:", s.min())
print("\nPatients above 60 years:")
print(s[s > 60])


#12.11.	Create a Pandas Series using a dictionary containing student names and attendance percentages.
import pandas as pd
attendance = {
    'MK': 80,
    'JK': 95,
    'RM': 68,
    'V': 92,
    'JM': 72
}
s = pd.Series(attendance)
print("Student Attendance:")
print(s)
print("\nAverage Attendance:", s.mean())
print("\nStudents with attendance below 75%:")
print(s[s < 75])
print("\nStudents with attendance above 90%:")
print(s[s > 90])
print("\nHighest Attendance:", s.max())


#13.12.	Dataset: students.csv
import pandas as pd
df = pd.read_csv('students.csv')
print("First 5 Records:")
print(df.head())
print("\nLast 5 Records:")
print(df.tail())
df['Total'] = df[['Python', 'DBMS', 'Maths']].sum(axis=1)
df['Average'] = df[['Python', 'DBMS', 'Maths']].mean(axis=1)
print("\nTotal and Average Marks:")
print(df)
print("\nStudents with average above 75:")
print(df[df['Average'] > 75])
print("\nStudent with Highest Average:")
print(df.loc[df['Average'].idxmax()])
print("\nSubject-wise Average Marks:")
print(df[['Python', 'DBMS', 'Maths']].mean())


#14.13.	Dataset: employees.csv
import pandas as pd
df = pd.read_csv('employees.csv')
print("Employees from CSE Department:")
print(df[df['Department'] == 'CSE'])
print("\nAverage Salary:", df['Salary'].mean())
print("Highest Salary:", df['Salary'].max())
print("Lowest Salary:", df['Salary'].min())
print("\nEmployees earning more than 50000:")
print(df[df['Salary'] > 50000])
print("\nDepartment-wise Average Salary:")
print(df.groupby('Department')['Salary'].mean())

#15.14.	Dataset: patients.csv
import pandas as pd
df = pd.read_csv('patients.csv')
print("Patients above 60 years:")
print(df[df['Age'] > 60])
print("\nAverage Medical Expense:")
print(df['Medical_Expense'].mean())
print("\nPatient with Highest Medical Expense:")
print(df.loc[df['Medical_Expense'].idxmax()])
print("\nNumber of Patients for Each Disease:")
print(df['Disease'].value_counts())
print("\nPatients with expenses above 50000:")
print(df[df['Medical_Expense'] > 50000])


#16.15.Dataset: weather.csv
import pandas as pd
df = pd.read_csv('weather.csv')
print("Maximum Temperature:", df['Temperature'].max())
print("Minimum Temperature:", df['Temperature'].min())
print("Average Temperature:", df['Temperature'].mean())
print("\nRecords with Temperature above 35°C:")
print(df[df['Temperature'] > 35])
print("\nCity-wise Average Temperature:")
print(df.groupby('City')['Temperature'].mean())
