print("Find length of string without using len()")
s=input("Enter a string:")
count=0
for ch in s:
    count+=1
print("Length of string:",count)



print("Count vowels, consonants, digits, spaces, and special characters")
s=input("Enter a string: ")
v=c=d=sp=spe=0
for ch in s:
    if ch.lower() in "aeiou":
        v+= 1
    elif ch.isalpha():
        c+= 1
    elif ch.isdigit():
        d+= 1
    elif ch.isspace():
        sp+= 1
    else:
        spe+= 1
print("Vowels:", v, "Consonants:", c, "Digits:", d, "Spaces:", sp, "Special:", spe)


print("Reverse a string without using built-in reverse")
s=input("Enter a string: ")
rev=""
for ch in s:
    rev=ch+rev
print("Reversed string:", rev)

print("Check if string is palindrome")
s= input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")



print("Count uppercase and lowercase letters")
s = input("Enter a string: ")
upper = lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase:", upper, "Lowercase:", lower)



print("Replace all occurrences of a character")
s = input("Enter a string: ")
old = input("Character to replace: ")
new = input("New character: ")
result = ""
for ch in s:
    if ch == old:
        result += new
    else:
        result += ch
print("Modified string:", result)



print("Remove all spaces from string")
# Program 7: Remove all spaces from string
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch != " ":
        result += ch
print("String without spaces:", result)



print("Find frequency of a character")
s = input("Enter a string: ")
ch = input("Enter character: ")
count = 0
for c in s:
    if c == ch:
        count += 1
print("Frequency of", ch, ":", count)




print("Print first and last character")
s = input("Enter a string: ")
print("First character:", s[0])
print("Last character:", s[-1])




print("Display ASCII values of characters")
s = input("Enter a string: ")
for ch in s:
    print(ch, ":", ord(ch))



print("Count words in a sentence")
s = input("Enter a sentence: ")
words = s.split()
print("Word count:", len(words))



print("Find longest word in sentence")
s = input("Enter a sentence: ")
words = s.split()
longest = max(words, key=len)
print("Longest word:", longest)



print("Find shortest word in sentence")
s = input("Enter a sentence: ")
words = s.split()
shortest = min(words, key=len)
print("Shortest word:", shortest)



print("Convert first letter of each word to uppercase")
s = input("Enter a sentence: ")
words = s.split()
result = ""
for w in words:
    result += w[0].upper() + w[1:].lower() + " "
print("Title case:", result.strip())



print("Print duplicate characters")
s = input("Enter a string: ")
seen = set()
duplicates = set()
for ch in s:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)
print("Duplicate characters:", "".join(duplicates))



print("Display frequency of each character")
s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
for k, v in freq.items():
    print(k, ":", v)



print("Check if two strings are anagrams")
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")



print("Remove duplicate characters")
s = input("Enter a string: ")
result = ""
seen = set()
for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)
print("Without duplicates:", result)




print("Check if substring exists")
s = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in s:
    print("Substring exists")
else:
    print("Substring not found")




print("Count occurrences of a word")
s = input("Enter a sentence: ")
word = input("Enter word: ")
words = s.split()
count = 0
for w in words:
    if w == word:
        count += 1
print("Occurrences of", word, ":", count)







