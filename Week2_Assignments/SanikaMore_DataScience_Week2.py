##Task 1: Basic Operations

# Taking two integer inputs from the user
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# Performing arithmetic operations
add = num1 + num2          # Addition
sub = num1 - num2          # Subtraction
mul = num1 * num2          # Multiplication
div = num1 / num2          # Division
mod = num1 % num2          # Modulus (remainder)
exp = num1 ** num2         # Exponentiation (power)

# Displaying results using formatted strings (f-strings)
print("\n--- Task 1 Results ---")
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
print(f"Modulus: {mod}")
print(f"Exponentiation: {exp}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##Task 2: Working with Lists and Arrays

# Creating a list
numbers = [10, 25, 5, 40, 60, 15, 30, 80, 55, 20]

# Length of list
print("Length of list:", len(numbers))

# Max and Min
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

# Adding and removing elements
numbers.append(100)
numbers.remove(5)

# Sorting
numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)

import numpy as np

arr = np.array(numbers)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##Task 3: Dictionaries and Sets

# Creating dictionary
student = {
    "name": "Sanika",
    "age": 21,
    "course": "Data Science",
    "marks": 85
}

# Printing key-value pairs
print("Student Details:")
for key, value in student.items():
    print(f"{key}: {value}")
    
# Adding new key
student["grade"] = "A"

# Creating set (duplicates removed automatically)
courses = {"Python", "Data Science", "AI", "Python"}
print("Unique Courses:", courses)

# Set operations
set1 = {"Python", "AI", "ML"}
set2 = {"AI", "Data Science", "ML"}

print("Union:", set1.union(set2)) #combines elements from both sets without duplicates
print("Intersection:", set1.intersection(set2)) #returns only common elements present in both sets
print("Difference:", set1.difference(set2)) #returns elements that are in set1 but not in set2

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Task 4: File Handling

# Writing data to file
with open("student_data.txt", "w") as file:
    file.write("Amit,Data Science,82\n")
    file.write("Sneha,AI,90\n")
    file.write("Rahul,Python,70\n")
    file.write("Priya,ML,88\n")
    file.write("Rohan,Data Science,65\n")
    
# Reading file and filtering students with marks > 75
print("Students with marks above 75:")

with open("student_data.txt", "r") as file:
    for line in file:
        name, course, marks = line.strip().split(",")
        if int(marks) > 75:
            print(f"Name: {name}, Course: {course}, Marks: {marks}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------