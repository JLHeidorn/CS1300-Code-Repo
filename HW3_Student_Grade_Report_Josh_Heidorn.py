name = input("Enter student name: ")

e1 = int(input("Enter Exam 1 score: "))
e2 = int(input("Enter Exam 2 score: "))
e3 = int(input("Enter Exam 3 score: "))

avg = (e1 + e2 + e3) / 3

# Grade
if avg >= 90:
    grade = "A"
elif avg >= 87:
    grade = "A-"
elif avg >= 83:
    grade = "B+"
elif avg >= 80:
    grade = "B"
elif avg >= 77:
    grade = "B-"
elif avg >= 73:
    grade = "C+"
elif avg >= 70:
    grade = "C"
elif avg >= 67:
    grade = "C-"
elif avg >= 63:
    grade = "D+"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

# Status
if avg >= 90:
    status = "Dean's List"
elif avg >= 70:
    status = "Good Standing"
elif avg >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

print("\n============================")
print("STUDENT GRADE REPORT")
print("============================")
print("Student:", name)
print("Exam 1:", e1)
print("Exam 2:", e2)
print("Exam 3:", e3)
print("----------------------------")
print("Average:", round(avg, 2))
print("Grade:", grade)
print("Status:", status)
print("============================")