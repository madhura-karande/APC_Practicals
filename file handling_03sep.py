#1. Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.
f = open("student.txt", "w")
name = input("Enter name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")
f.write("Name: " + name + "\n")
f.write("Roll No: " + roll + "\n")
f.write("Branch: " + branch + "\n")
f.write("Semester: " + semester + "\n")
f.close()
print("Data written successfully")


#2.Write a program to open a text file and display its complete contents.
f = open("student.txt", "r")
data = f.read()
print(data)
f.close()


#3. Write a program to append additional student information to an existing file without deleting its previous contents
f = open("student.txt", "a")
f.write("College: DYPCET\n")
f.write("City: Kolhapur\n")
f.close()
print("Data appended successfully")


#4. Write a program to read a text file line by line and display each line separately.
f = open("student.txt", "r")
for line in f:
    print(line, end="")
f.close()


#5. Write a program to count and display the total number of lines present in a text file
f = open("student.txt", "r")
lines = f.readlines()
print("Total lines:", len(lines))   
f.close()


#6. Write a program to count the total number of words present in a text file.
f = open("student.txt", "r")
data = f.read()
words = data.split()
print("Total words:", len(words))
f.close()


#7. Write a program to count the total number of characters in a text file, including spaces.
f = open("student.txt", "r")
data = f.read()
print("Total characters:", len(data))
f.close()


#8. Write a program to read a text file and display its lines in reverse order.
f = open("student.txt", "r")
lines = f.readlines()
for line in reversed(lines):
    print(line, end="")
f.close()


#9. Read a text file and count the number of vowels and consonants present in the file.
f = open("student.txt", "r")
data = f.read().lower()
vowels = 0
consonants = 0
for ch in data:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
f.close()


#10.Read a text file and calculate the number of alphabets, digits, spaces, and special characters.
f = open("student.txt", "r")
data = f.read()
alphabets = 0
digits = 0
spaces = 0
special = 0
for ch in data:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1
print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)
f.close()


#11.Read a text file and find the longest word present in the file.
f = open("student.txt", "r")
words = f.read().split()
longest = max(words, key=len)
print("Longest word:", longest)
f.close()


#12.Read a text file and count how many times each word occurs. Display the result using a dictionary.
f = open("student.txt", "r")
words = f.read().lower().split()
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print("Word frequency:", count)
f.close()


#13.Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.
f = open("student.txt", "r")
word = input("Enter word to search: ")
count = 0
line_no = 0
for line in f:
    line_no += 1
    for w in line.split():
        if w == word:
            count += 1
            print("Found on line:", line_no)
print("Total occurrences:", count)
f.close()


#14.Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.
f =open("student.txt", "r")
data = f.read()
old = input("Enter word to replace: ")
new = input("Enter new word: ")
data = data.replace(old, new)
f.close()
f = open("student.txt", "w")
f.write(data)
f.close()
print("Word replaced successfully")


#15.Read a Python source file and create another file after removing single-line comments.
f = open("set_20aug.py", "r")
out = open("newfile_03sep.py", "w")
for line in f:
    if not line.strip().startswith("#"):
        out.write(line)
f.close()
out.close()
print("Single line comments removed successfully!!")


#16.Read a text file and create another file containing the same text in uppercase.
f = open("student.txt", "r")
out = open("uppercase.txt", "w")
data = f.read()
out.write(data.upper())
f.close()
out.close()
print("Uppercase file created successfully")


#17.Create a file containing student records in the format:
f = open("students.txt", "w")
f.write("101,Amit,85\n")
f.write("102,Priya,92\n")
f.write("103,Rahul,78\n")
f.close()
f = open("students.txt", "r")
total = 0
count = 0
highest = 0
highest_name = ""
print("All Records:")
for line in f:
    roll, name, marks = line.strip().split(",")
    marks = int(marks)
    print(roll, name, marks)
    total += marks
    count += 1
    if marks > highest:
        highest = marks
        highest_name = name
    if marks > 80:
        print("Scored more than 80:", name)
print("Highest Marks:", highest_name, highest)
print("Average Marks:", total / count)
f.close()


#18.Store employee ID, name, department, and salary in a file. 
f = open("employee.txt", "w")
f.write("101,Amit,IT,50000\n")
f.write("102,Priya,HR,60000\n")
f.write("103,Rahul,Sales,45000\n")
f.close()
f = open("employee.txt", "r")
total = 0
count = 0
highest = 0
highest_name = ""
print("All Employees:")
for line in f:
    empid, name, dept, salary = line.strip().split(",")
    salary = int(salary)
    print(empid, name, dept, salary)
    total += salary
    count += 1
    if salary > highest:
        highest = salary
        highest_name = name
print("Highest Paid Employee:", highest_name, highest)
print("Average Salary:", total / count)
f.seek(0)
limit = int(input("Enter salary limit: "))
print("Employees earning above", limit, ":")
for line in f:
    empid, name, dept, salary = line.strip().split(",")
    salary = int(salary)
    if salary > limit:
        print(name, salary)
f.close()


#19.Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.
f = open("attendance.txt", "w")
f.write("Amit,80,100\n")
f.write("Priya,70,100\n")
f.write("Rahul,90,100\n")
f.close()
f = open("attendance.txt", "r")
for line in f:
    name, present, total = line.strip().split(",")
    present = int(present)
    total = int(total)
    percentage = (present / total) * 100
    print(name, "Attendance:", percentage, "%")
    if percentage < 75:
        print("Attendance below 75%")
f.close()


#20.Store deposits and withdrawals in a file. Read the file and calculate: 
f = open("transactions.txt", "w")
f.write("deposit,5000\n")
f.write("withdraw,1000\n")
f.write("deposit,3000\n")
f.write("withdraw,500\n")
f.close()
f = open("transactions.txt", "r")
deposits = 0
withdrawals = 0
largest = 0
for line in f:
    typ, amount = line.strip().split(",")
    amount = int(amount)
    if typ == "deposit":
        deposits += amount
    else:
        withdrawals += amount
    if amount > largest:
        largest = amount
print("Total Deposits:", deposits)
print("Total Withdrawals:", withdrawals)
print("Final Balance:", deposits - withdrawals)
print("Largest Transaction:", largest)
f.close()

#21.Maintain book records containing book ID, title, author, and availability status. Implement operations to: 
books = {}
while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        books[book_id] = [title, "Available"]
        print("Book added")
    elif choice == 2:
        book_id = input("Enter Book ID: ")
        if book_id in books:
            print("Book:", books[book_id])
        else:
            print("Book not found")
    elif choice == 3:
        book_id = input("Enter Book ID: ")
        if book_id in books:
            books[book_id][1] = "Issued"
            print("Book issued")
        else:
            print("Book not found")
    elif choice == 4:
        book_id = input("Enter Book ID: ")
        if book_id in books:
            books[book_id][1] = "Available"
            print("Book returned")
        else:
            print("Book not found")
    elif choice == 5:
        print("Available Books:")
        for book_id, details in books.items():
            if details[1] == "Available":
                print(book_id, details[0])
    elif choice == 6:
        print("Exit")
        break


#22.Read the contents of two text files and create a third file containing the contents of both files.
f1=open("student.txt","r")
f2=open("newfile_03sep.py","r")
f3=open("file3.txt","w")
f3.write(f1.read())
f3.write(f2.read())
f1.close()
f2.close()
f3.close()
print("Files merged successfully")



#23.Write a program to compare two text files and display whether their contents are identical. If different, identify the first line where they differ.
f1 = open("student.txt", "r")
f2 = open("file3.txt", "r")
lines1 = f1.readlines()
lines2 = f2.readlines()
if lines1 == lines2:
    print("Files are identical")
else:
    print("Files are different")
    for i in range(min(len(lines1), len(lines2))):
        if lines1[i] != lines2[i]:
            print("First difference is at line:", i + 1)
            break
    if len(lines1) != len(lines2):
        print("The files have different numbers of lines.")
f1.close()
f2.close()








