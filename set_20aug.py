#1. Write a Python program to create a set containing five integers and display all its elements.

set1={13,7,2,25,9}
print(set1)


#2. Create a list containing duplicate values. Convert the list into a set and display the resulting set.
list1=[10,12,11,67,11,10]
print("List")
print(list1)
set1=set(list1)
print("\nSet")
print(set1)


#3. Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
s1={"apple","guava","cherry","banana","papaya"}
print(s1)
s1.add("Strawberry")
s1.add("mango")
print()
print("updated")
print(s1)


#4. Create a set of numbers and remove a specified number from the set.
s={89,18,67,22,11}
s.remove(22)
print(s)


#5. Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
s={"MK","RM","JM","JIN","V","JK"}
st=input("Enter name: ")
if st in s:
    print("Name exists")
else:
    print("Not in the list")


#6. Create a set of cities and determine the total number of cities using an appropriate function.
city={"satara","pune","karad","kolhapur","sangli"}
print(city)
print(len(city))


#7. Create a set of programming languages and display each language using a for loop.
prg={"java","c","c++","python","ruby","html"}
for i in  prg:
    print(i)


#8. Create a list containing duplicate numbers, use a set to remove the duplicates.
list1=[10,12,11,67,11,10]
print("List")
print(list1)
set1=set(list1)
print("\nSet")
print(set1)


#9. Create two sets of integers and find their union
s1={7,98,45,32,11,90}
s2={45,90,67,32,88,40}
print(s1)
print(s2)
print("union",s1.union(s2))


#10.Create two sets and find the elements common to both sets.
s1={7,98,45,32,11,90}
s2={45,90,67,32,88,40}
print(s1)
print(s2)
print("intersection",s1.intersection(s2))


#11.Create two sets and find:
#•Elements present in the first set but not the second 
#•Elements present in the second set but not the first
s1={7,98,45,32,11,90}
s2={45,90,67,32,88,40}
print(s1)
print(s2)
print("Elements present in the first set but not the second  ",s1-s2)
print("Elements present in the second set but not the first  ",s2-s1)



#12.Create two sets of numbers and find the elements that are present in either set but not in both.
s1={7,98,45,32,11,90}
s2={45,90,67,32,88,40}
print(s1)
print(s2)
print("no in both",s1^s2)


#13.Create two sets and determine whether the first set is a subset of the second set.
s1={7,98,45,32,11,90}
s2={45,90,67,32,11,88,40}
print(s1)
print(s2)
print("subset or not: ",s1.issubset(s2))


#14.Create two sets and determine whether the first set is a superset of the second set.
s1={7,98,45,32,11,90}
s2={45,90,67,32,11,88,40}
print(s1)
print(s2)
print("superset or not: ",s2.issuperset(s1))


#15.Write a program to determine whether two sets have no elements in common.
s1={7,98,45,32,11,90}
s2={45,90,67,32,11,88,40}
print(s1)
print(s2)
print("common or not: ",s1.isdisjoint(s2))


#16.Create two sets and check whether they are equal.
s1={32,11,90}
s2={32,11,90}
print(s1)
print(s2)
print("equal or not: ",s1==s2)


#17.Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
student1={"maths","english","history","science","physics","biology"}
student2={"c","c++","cn","science","maths"}
print(student1)
print(student2)
print("Same subjects:",student1.intersection(student2))


#18.Accept a sentence from the user and use a set to display all unique words.
sen=input("Enter sentence:")
u=set(sen.split())
print(u)


#19.Create two sets perform operations:
m={"mk","jm","jk","vp"}
a={"jin","v","mk","vp"}
print("Students present in both sessions: ",m.union(a))
print("Students present only in the morning: ",m)
print("Students present only in the afternoon: ",a)
print("Students present in at least one session: ",m.intersection(a))


#20.Create sets representing students enrolled in: Python, Java
python={"mk","jm","jk","vp"}
java={"jin","v"}
print(python)
print(java)


#21.Find students enrolled in both courses and students enrolled in only one course.
python={"mk","jm","jk","vp"}
java={"jin","v","jk","mk"}
print("bothe courses: ",python.intersection(java))
print("only one course: ",python^java)



#22.Create two sets representing technical skills of two employees. Find:
employee1 = {"Python", "Java", "SQL", "HTML"}
employee2 = {"Python", "C++", "SQL", "CSS"}
print("Common skills:", employee1 & employee2)
print("Unique to Employee 1:", employee1 - employee2)
print("Unique to Employee 2:", employee2 - employee1)
print("All available skills:", employee1 | employee2)

#23.Create a set containing available books and another set containing requested books. Determine which requested books are available.
available_books = {"Python", "Java", "C++", "DBMS"}
requested_books = {"Python", "DBMS", "HTML"}

print("Available requested books:", available_books & requested_books)


#24.Store visitor IDs from two different days in separate sets. Determine:
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)
category1 = {"Laptop", "Mobile", "Tablet", "Camera"}
category2 = {"Mobile", "Tablet", "Smartwatch", "Camera"}
print("Products in both categories:", category1 & category2)


#25.Represent the friends of two users using sets. Find:
user1 = {"mk", "RM", "jm", "jk"}
user2 = {"jm", "v", "mk", "sg"}
print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", user1 | user2)
