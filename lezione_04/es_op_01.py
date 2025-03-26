'''School Grading System:
Create a function that takes a student's name and their scores in different subjects as input.
The function calculates the average score and prints the student's name, average, 
and a message indicating whether the student passed the exam (average >= 60) or failed.
Create a for loop to iterate over a list of students and scores, calling the function for each student.
'''

def grade_student(name, scores):
    # Calculate the average score
    average_score = sum(scores) / len(scores)
    
    # Determine pass or fail
    status = "Passed" 
    if average_score >= 60:
        status = "Passed"
    else:
        status = "Failed"
    
    # Print the student's name, average score, and status
    print(f"Student: {name}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Status: {status}")
    print("-" * 30)

# List of students with their scores
students_scores = [
    ("Alice", [85, 90, 78]),
    ("Bob", [55, 60, 65]),
    ("Charlie", [45, 50, 55]),
    ("David", [88, 92, 80])
]

# Iterate over the list of students and call the function for each
for student, scores in students_scores:
    grade_student(student, scores)

    
