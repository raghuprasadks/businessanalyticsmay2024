def grade(marks):
    grade =''
    if(marks > 90 and marks <= 100):
        grade ='A+'
    elif (marks > 80 and marks <= 90):
        grade = 'A'
    elif (marks > 70 and marks <= 80):
        grade = 'B+'
    elif (marks > 60 and marks <= 70):
        grade = 'B'
    else:
        grade = 'C'
    print("your grade is ",grade)
marks = int(input("Enter your marks"))
grade(marks)

