#1.Write a Python program to create a list of five fruits and display the list.
'''
fruits=["Apple","Banana","Cherry","Mango","papaya"]
for i in fruits:
    print(i)

    
#2. Create a list of five integers. Display:
#•	First element 
#•	Last element 
#•	Third element
lst=[13,7,25,20,2]
print("First element",lst[0])
print("Last element",lst[4])
print("Third element",lst[2])



#3. Create a list of colors. Replace the third color with another color and display the updated list.
color=["red","blue","white","black","yellow"]
print("before:")
for i in color:
    print(i)
print()
print("after:")
color[3]="purple"
for i in color:
    print(i)



#4. Create a list of numbers. Add:
#•One element at the end 
#•One element at the beginning 
#•One element at a specified position

lst=[13,7,25,20,2]
for i in lst:
    print(i,end=" ")
lst.append(3)
lst.insert(0,10)
lst.insert(3,15)
print()
for i in lst:
    print(i,end=" ")



#5. Create a list of student names. Remove:
#•  First student 
#•  Last student 
#•  A specific student by name 


student=['jk','madhura','vaishnavi','jm','shreya','sharavni','piyusha','mk']
for i in student:
    print(i,end=" ")
student.pop()
student.remove('jk')
student.remove('jm')
print()
for i in student:
    print(i,end=" ")



#6. Write a program to find the largest and smallest number in a list without using max() or min().
num=[12, 45, 7, 89, 23]
l=num[0]
s=num[0]
for i in num:
    if i>l:
        l=i
    if i<s:
        s=i
print("Largest number:", l)
print("Smallest number:", s)




#7. Accept 10 numbers from the user and store them in a list. Calculate:
#•   Sum 
#•   Average 

numbers=[]

for i in range(10):
    num=int(input("Enter a number: "))
    numbers.append(num)
total=sum(numbers)
average=total/10
print("List:",numbers)
print("Sum =",total)
print("Average =",average)



#8. Store 15 integers in a list. Count how many numbers are:
#•   Even 
#•   Odd


#8. Store 15 integers and count even and odd numbers

numbers=[]
for i in range(15):
    num=int(input("Enter a number: "))
    numbers.append(num)
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers =", even)
print("Odd numbers =", odd)



#9. Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.

cities=["Pune", "Mumbai", "Delhi", "Chennai", "Hyderabad"]
city=input("Enter a city name: ")
if city in cities:
    print("City found in the list")
else:
    print("City not found in the list")



#10.Write a program to reverse a list without using the reverse() method.
numbers=[10, 20, 30, 40, 50]
reversed_list=[]
for i in range(len(numbers)-1,-1,-1):
    reversed_list.append(numbers[i])
print("Original List:",numbers)
print("Reversed List:",reversed_list)




#11.	Create a list of 10 numbers and display:
#•	First 5 elements 
#•	Last 5 elements 
#•	Middle 4 elements 
#•	Alternate elements 
#•	Reverse list using slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse list:", numbers[::-1])



#12.Display all elements present at even index positions.
numbers=[10, 20, 30, 40, 50, 60, 70, 80]
print("Elements at even index positions:")
for i in range(0,len(numbers),2):
    print(numbers[i])



#13.	Accept 10 numbers and sort them in:
#•	Ascending order 
#•	Descending order
numbers=[]
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
numbers.sort()
print("Ascending order:", numbers)
numbers.sort(reverse=True)




#14.	Create a list containing duplicate values and display only unique elements.
numbers=[10, 20, 30, 20, 40, 10, 50, 30]
unique=list(set(numbers))
print("Original List:", numbers)
print("Unique Elements:", unique)



#15.	Find the second largest element in a list.
numbers=[10, 50, 30, 80, 60]
numbers.sort()
print("Second largest element:", numbers[-2])


#16.	Create a nested list storing:
#•	Student Name 
#•	Roll Number 
#•	Marks 
#Display all student details
students=[
    ["Rahul", 1, 85],
    ["Priya", 2, 90],
    ["Amit", 3, 78]
]
print("Student Details:")
for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()



#17.	Create two 3 × 3 matrices using nested lists and perform matrix addition.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
C = []
for i in range(3):
    row=[]
    for j in range(3):
        row.append(A[i][j]+B[i][j])
    C.append(row)
print("Matrix Addition:")
for row in C:
    print(row)




#18.	Create a shopping cart using a list.
#Perform:
#•	Add item 
#•	Remove item 
#•	Search item 
#•	Display cart 
#•	Count total items
cart=["Milk", "Bread", "Eggs"]
item=input("Enter item to add: ")
cart.append(item)
item=input("Enter item to remove: ")
if item in cart:
    cart.remove(item)
else:
    print("Item not found")
item=input("Enter item to search: ")
if item in cart:
    print("Item found")
else:
    print("Item not found")
print("Shopping Cart:", cart)
print("Total items:", len(cart))



#19.	Store names of students present in class.
#Display:
#•	Total students 
#•	Search a student's attendance 
#•	Add a new student 
#•	Remove an absent student 
students=["Rahul", "Priya", "Amit", "Sneha"]
print("Total Students:", len(students))
name = input("Enter student name to search: ")
if name in students:
    print("Student Present")
else:
    print("Student Not Present")
new=input("Enter new student name: ")
students.append(new)
remove=input("Enter absent student name: ")
students.remove(remove)
print("Updated Student List:", students)



#20.	Create a list of books.
#Implement:
#•	Add a new book 
#•	Search a book 
#•	Remove a book 
#•	Display all books 
#•	Count total books
books=["Python", "Java", "C"]
books.append("HTML")          
print(books)
if "Python" in books:         
    print("Book Found")
books.remove("Java")          
print(books)
print("All Books:", books)    
print("Total Books:", len(books))   




#21.	Accept two lists and merge them into a single list.
list1=input("Enter first list elements: ").split()
list2=input("Enter second list elements: ").split()
list3=list1+list2
print("Merged List:", list3)




#22.	Find common elements between two lists
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

for i in list1:
    if i in list2:
        print(i)


#23.	Count the frequency of each element in a list.
numbers=[10, 20, 10, 30, 20, 10]
for i in numbers:
    print(i, "=", numbers.count(i))


#24.	Rotate a list:
#•	Left by one position 
#•	Right by one position

numbers=[10, 20, 30, 40, 50]
left=numbers[1:] + numbers[:1]
print("Left Rotation:", left)
right = numbers[-1:] + numbers[:-1]
print("Right Rotation:", right)



#25.	Remove all duplicate elements while preserving the original order.
numbers=[10, 20, 10, 30, 20, 40]
unique=[]
for i in numbers:
    if i not in unique:
        unique.append(i)
print("Original List:", numbers)
print("List without duplicates:", unique)



#26.	Store marks of 20 students in a list and determine:
#•	Highest marks 
#•	Lowest marks 
#•	Average marks 
#•	Number of students scoring above average 
#•	Number of students scoring below average
marks=[]
for i in range(20):
    m=int(input("Enter marks: "))
    marks.append(m)
highest=max(marks)
lowest=min(marks)
average=sum(marks)/len(marks)
above=0
below=0
for i in marks:
    if i>average:
        above+=1
    elif i<average:
        below+=1
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Above Average:", above)
print("Students Below Average:", below)
'''


#27.	Store salaries of employees and determine:
#•	Highest salary 
#•	Lowest salary 
#•	Average salary 
#•	Employees earning above ₹50,000 
#•	Employees earning below ₹30,000 
salary = []
for i in range(5):
    s = int(input("Enter salary: "))
    salary.append(s)
highest = max(salary)
lowest = min(salary)
average = sum(salary) / len(salary)
above = 0
below = 0

for i in salary:
    if i > 50000:
        above += 1
    if i < 30000:
        below += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees earning above 50000:", above)
print("Employees earning below 30000:", below)
