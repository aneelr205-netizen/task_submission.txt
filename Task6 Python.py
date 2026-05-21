#Task1 
# LIST OPERATIONS 

Marks = [78, 85, 92, 67, 88, 90, 76, 85, 95, 80]
Marks.append(89)
Marks.append(73)
Marks.insert(1, 81)
Marks.remove(67)
Marks.pop()

print("Updated Marks List: ", Marks)
print("Highest Mark: ", max(Marks))
print("Lowest Mark: ", min(Marks))
print("Number of times 85 appears: ", Marks.count(85))
print("Position of 92: ", Marks.index(92))

Marks.sort()
print("Ascending Order: ", Marks)

Marks.reverse()
print("Descending Order: ", Marks)


#Task2 
# Tuple Operations

employee = ("Ram", 33, "Software Engineer")
name, age, profession = employee
print("Employee Name: ", name)
print("Employee Age: ", age)
print("Employee Profession: ", profession)

#Task3
# Set Operations

online_courses = {"Python", "Data Science", "Machine Learning", "Web Development"}
completed_courses = {"Python", "Data Science"}
print("Union: ", online_courses.union(completed_courses))
print("Intersection: ", online_courses.intersection(completed_courses))
print("Difference: ", online_courses.difference(completed_courses))


#Task4
# Dictionary Operations

students = {
    "student Name": "Teja",
    "Department": "Computer Science",
    "CGPA": 9.0,
    "City": "bangalore"
}

print("Keys: ", students.keys())
print("Values: ", students.values())
print("Items: ", students.items())
