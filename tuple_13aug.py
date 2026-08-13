#1.Write a Python program to create a tuple of five integers and display it.
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)

#2. Create a tuple containing five city names. Display:
#•First city 
#•Last city 
#•Third city
city=("Satara","Karad","Kolhapur","Pune","Sangli")
print("First city:",city[0])
print("Last city:",city[-1])
print("Third city:",city[2])

#3. Create a tuple of student names and display the total number of students using the len() function.
students = ("Madhura", "Vaishnavi", "Piyusha", "Shravani", "Shreya")
print("Total students:", len(students))


#4. Create a tuple of colors. Check whether a given color exists in the tuple
colors = ("Red", "Blue", "Green", "Yellow", "Black")
color = input("Enter a color: ")
if color in colors:
    print("Color exists")
else:
    print("Color does not exist")


#5. Create a tuple of fruits and display each fruit using a loop.
fruits=("Apple","Banana","Cherry","Strawberry","Guava")
for i in fruits:
    print(i)


#6. Create a tuple with repeated numbers and count how many times a particular number appears
numbers = (10, 20, 10, 30, 10, 40, 20)
number = int(input("Enter number: "))
print("Count:", numbers.count(number))


#7. Create a tuple of employee IDs and find the index of a given ID.
emp=(128,113,112,111,124,132)
id=int(input("Enter ID to search its index:"))
if id in emp:
    print(emp.index(id))
else:
    print("ID not found")


#8. Create two tuples of numbers and concatenate them into a single tuple.
t1=(1,20,30,40)
t2=(60,70,80,90)
print("Concatenated tuples:",t1+t2)

#9. Create a tuple containing three elements and repeat it four times.
num= (1, 2, 3)
result = num*4
print(result)

#10.Create a tuple of 10 numbers and display:
#•First five elements 
#•Last five elements 
#•Middle four elements 
#•Alternate elements 
#•Reverse tuple
tup=(1,20,30,40,50,60,70,80,90,100)
print("First five:", numbers[:5])
print("Last five:", numbers[5:])
print("Middle four:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse:", numbers[::-1])


#11.Convert a tuple into a list and add a new element.
t=(13,7,20,10,24)
t_1=list(t)
print(t_1.append(2))
print(t_1)


#12.Accept five numbers from the user, store them in a list, and convert the list into a tuple.
numbers = []
for i in range(5):
    number = int(input("Enter number: "))
    numbers.append(number)
numbers = tuple(numbers)
print("Tuple:", numbers)


#13.Modify a tuple by converting it into a list and then back into a tuple.
numbers = (10, 20, 30, 40)
numbers_list = list(numbers)
numbers_list[1] = 25
numbers = tuple(numbers_list)
print("Modified tuple:", numbers)


#14.Create a tuple and delete it completely
numbers = (10, 20, 30, 40)
print("Tuple:", numbers)
del numbers
print("Tuple deleted successfully")


#15.Create a nested tuple containing student details and display each record.
students = (
    (1, "Rahul", 85),
    (2, "Sneha", 90),
    (3, "Amit", 78)
)
for student in students:
    print(student)

#16.Store ten numbers in a tuple and calculate their sum.
numbers = (10, 20, 30, 40, 50)
total = sum(numbers)
print("Sum:", total)

#17.Find the largest and smallest number in a tuple without using max() and min().
numbers = (25, 10, 45, 5, 30)
largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
print("Largest:", largest)
print("Smallest:", smallest)


#18.Calculate the average of elements stored in a tuple.
numbers = (10, 20, 30, 40, 50)
total = sum(numbers)
average = total / len(numbers)
print("Average:", average)

#19.Store 15 integers in a tuple and count:
#•Even numbers 
#•Odd numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)


#20.Accept a number from the user and determine whether it exists in the tuple.
numbers = (10, 20, 30, 40, 50)
number = int(input("Enter number: "))
if number in numbers:
    print("Number exists")
else:
    print("Number does not exist")


#21.Store student details in a tuple:
#•Roll Number 
#•Name 
#•Department 
#•Marks 
#Display all the details.
student = (128, "Madhura Karande", "CSE", 85)
print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])


#22.Create tuples containing:
#•Employee ID
#•Name 
#•Salary
employees = (
    (101, "MK", 30000),
    (102, "JK", 35000),
    (103, "RM", 40000)
)
for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()



#23.Store item prices in a tuple and calculate:
#•Total bill 
#•Average price 
#•Highest-priced item 
#•Lowest-priced item
prices = (100, 250, 150, 500, 300)
total = sum(prices)
av= total / len(prices)
h= prices[0]
l= prices[0]
for price in prices:
    if price > h:
        h= price
    if price < l:
        l= price

print("Total bill:", total)
print("Average price:", av)
print("Highest price:", h)
print("Lowest price:", l)


#24.Store temperatures of seven days in a tuple and determine:
#•Maximum temperature 
#•Minimum temperature 
#•Average temperature 
temperatures = (30, 32, 29, 35, 31, 28, 33)
print("Maximum temperature:", max(temperatures))
print("Minimum temperature:", min(temperatures))
print("Average temperature:", sum(temperatures) / len(temperatures))


#25.Store runs scored in 10 matches and calculate:
#•Total runs 
#•Highest score 
#•Lowest score 
#•Average score 
runs = (45, 60, 32, 78, 55, 90, 40, 65, 70, 50)
print("Total runs:", sum(runs))
print("Highest score:", max(runs))
print("Lowest score:", min(runs))
print("Average score:", sum(runs) / len(runs))


#26.Create two tuples and find the common elements between them
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
common = ()
for number in tuple1:
    if number in tuple2:
        common = common + (number,)
print("Common elements:", common)


#27.Merge two tuples and remove duplicate elements.
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
result = tuple(set(tuple1 + tuple2))
print("Merged tuple:", result)


#28.Count the frequency of each element in a tuple.
numbers = (1, 2, 2, 3, 3, 3, 4, 4)
for number in set(numbers):
    print(number, "appears", numbers.count(number), "times")


#29.Convert a tuple into a sorted tuple in ascending and descending order.
numbers = (40, 10, 50, 20, 30)
ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))
print("Ascending:", ascending)
print("Descending:", descending)


#30.Create a tuple containing patient records:
patients = (
    (101, "MK", 25, "A+"),
    (102, "JK", 30, "B+"),
    (103, "RM", 22, "A+"),
    (104, "JM", 28, "O+")
)

print("All Patient Records:")
for patient in patients:
    print(patient)
id = int(input("\nEnter Patient ID: "))
for patient in patients:
    if patient[0] == id:
        print("Patient found:", patient)
        break
else:
    print("Patient not found")
print("\nTotal patients:", len(patients))
blood_group = input("\nEnter blood group: ")
print("Patients with", blood_group, "blood group:")
for patient in patients:
    if patient[3] == blood_group:
        print(patient)
