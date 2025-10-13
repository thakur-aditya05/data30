# Dictionary banate hain: student name → marks

# initializing a dictionary
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 96,
    "Eva": 89 
}

# Method 1: loop se manually karna
highest_name = None
highest_marks = -1

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name
print(f"(Loop method) Student with highest marks: {highest_name} ({highest_marks} marks)")





# Method 2: builtin functions ka use karke
# max() mein key parameter denge taki value pe compare kare
# isska matlab hai ki maximum value find krni hai 
best_student = max(students, key=students.get)
# student mil jane ke baad uske marks nikal lenge 
best_marks = students[best_student]

print(f"Student with highest marks: {best_student} ({best_marks} marks)")







# example for each data Data Structures
# Lists – Creating lists, indexing, slicing, common methods (append, remove, sort,reverse) 
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])   # "apple" (first item)
print(fruits[3])   # "date"
print(fruits[-1])  # "date" (last item)
# slicing 
sub = fruits[1:3]
print(sub)  # ["banana", "cherry"]

fruits.append("elderberry")
print(fruits)  # ["apple", "banana", "cherry", "date", "elderberry"]

fruits.remove("banana")
print(fruits)  # ["apple", "cherry", "date", "elderberry"]

fruits.sort()
print(fruits)  # sorted alphabetically

fruits.reverse()
print(fruits)  # reversed order



# tuple 
person = ("Alice", 25, "Engineer")
name = person[0]   # "Alice"
age = person[1]    # 25




# unpacking
name, age, profession = person
print(name)        # "Alice"
print(profession)  # "Engineer"



# sets
s = {1, 2, 3, 4, 2, 3}
print(s)  # {1, 2, 3, 4} — duplicates hata diye gaye
s.add(5)    # add element 5
s.remove(2) # remove element 2


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))         # {1,2,3,4,5,6}
print(a.intersection(b))  # {3,4}
print(a.difference(b))    # {1,2}  — present in a but not in b



# dictionary
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
print(student_marks["Bob"])  # 92
print(student_marks.keys())    # dict_keys(["Alice", "Bob", "Charlie"])
print(student_marks.values())  # dict_values([85, 92, 78])
print(student_marks.items())   # dict_items([("Alice",85), ("Bob",92), ("Charlie",78)])

# get with default
print(student_marks.get("David", "No such student"))  # "No such student"

