string1 = "Hello "
string2 = input("Enter your Name: ")

print(string1 + string2)
string3= ", welcome to Python programming"
string4= string1 + string2 + string3
print(string4)

string1="Hello"
string2 = input("Enter your Name: ")

string3 = ", welcome to Python programming"
string4 = string1 + string2 + string3

print("Original String:", string4)

print("first character:", string4[0])

print("last character:", string4[-1])

print("First 5 characters:", string4[:5])

print("last 11 characters:", string4[-11:])

print("string in reverse:", string4[::-1])

print("Python:", string4[22:28])


strM= "Python beginner tutorial"

print("Uppercase:", strM.upper())

print("Lowercase:", strM.lower())

print("Capitalize:", strM.capitalize())

print("Count of t:", strM.count('t'))

print("Replace:", strM.replace("Python", "Machine Learning"))

t1 = (10, 20, 30)
t2 = (40, 50, 60)
t_combine = t1 + t2

print("Concatenate two tuples:", t_combine)

print("Repeat tuple:", t_combine * 3)

print("3rd element:", t_combine[2])


print("First three elements:", t_combine[:3])

print("Last three elements:", t_combine[-3:])



