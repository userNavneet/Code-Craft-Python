# Function to input marks for a student
def input_marks():
    marks = {}
    for subject in subjects:
        marks[subject] = int(input(f"Enter marks for {subject}: "))
    return marks

# Function to calculate maximum, minimum, and average marks
def calculate_stats(marks):
    max_marks_subject = max(marks, key=marks.get)
    max_marks = marks[max_marks_subject]
    min_marks_subject = min(marks, key=marks.get)
    min_marks = marks[min_marks_subject]
    average_marks = sum(marks.values()) / len(marks)
    return max_marks_subject, max_marks, min_marks_subject, min_marks, average_marks

# List of subjects
subjects = ['DBMS', 'Mathematics', 'Programming', 'Operating System', 'Computer Networks']

# Dictionary to store students' marks
students = {}

# Taking input for multiple students
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    student_name = input(f"Enter name of student {i+1}: ")
    print(f"Enter marks for {student_name}:")
    students[student_name] = input_marks()

# Calculating stats for each student
for student_name, marks in students.items():
    print(f"\nStatistics for {student_name}:")
    max_sub, max_marks, min_sub, min_marks, avg_marks = calculate_stats(marks)
    print("Maximum Marks:")
    print("Subject:", max_sub)
    print("Marks:", max_marks)
    print("\nMinimum Marks:")
    print("Subject:", min_sub)
    print("Marks:", min_marks)
    print("\nAverage Marks:", avg_marks)
    print("--------------------")
