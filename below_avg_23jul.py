print("Write a PYTHON program that reads a value of n and check the number is zero or non zero value.")

n=int(input("Enter any Number:"))
if n==0:
    print("Number is zero.")
else:
    print("Number is non zero.")



print("Write a PYTHON program to find a largest of two numbers.")

a1=int(input("Enter first number: "))
a2=int(input("Enter second number:"))
if a1>a2:
    print(a1,"is greater")
elif a1<a2:
    print(a2," is greater")
else:
    print("both numbers are equal")


print("Write a PYTHON program that reads the number and check the no is positive or negative.")

n=int(input("Enter any Number:"))
if n>=0:
    print("Number is Positive.")
else:
    print("Number is negative.")


print("Write a PYTHON program to check entered character is vowel or consonant.")
s=input("Enter character:")
if s=='a'or s=='e'or s=='i'or s=='o'or s=='u':
    print("character is vowel")
else:
    print("Character is constant")
