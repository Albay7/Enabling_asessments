#Write a program that will input grade with table and solution 
#Two Dimentional array
#Storing Lists
students = []
Quiz1 = []
Quiz2 = []
Quiz3 = []
finalExam = []
classParti = []
Grades = []
Result = []
numResult = []
P_or_F = []

#Inputs
while (True):
    Students = input("Write the name of the Student: ")
    Q1 = float(input("Write the score of Quiz # 1: "))
    Q2 = float(input("Write the score of Quiz # 2: "))
    Q3 = float(input("Write the score of Quiz # 3: "))
    FinalExam = float(input("Write the score of Final Exam: "))
    ClassParti = float(input("Write the score of Class Participation: "))
    students.append(Students)
    Quiz1.append(Q1)
    Quiz2.append(Q2)
    Quiz3.append(Q3)
    finalExam.append(FinalExam)
    classParti.append(ClassParti)


#Computation
    passingScore = 70
    Qtotal = ((Q1 + Q2 + Q3) / 3) * 0.4
    TotalExam = FinalExam * 0.4
    TotalClass = ClassParti * 0.2
    TotalGrade = Qtotal + TotalClass + TotalExam * 1
    Grades.append(TotalGrade)


    for score in Grades:
        if TotalGrade >= passingScore:
            result = ("PASSED")
        else:
            result = ("FAILED")
        Result.append(result)



    #Continuation of the program
    Prompt = input("Do you wish to continue? answer y or n\n")
    if Prompt == 'y':
        continue
    else:
        break

#Printing of the program output
print("Student Name | Quiz 1 | Quiz 2 | Quiz 3 | Final Exam | Class Participation | Average | Remarks ")
print("-------------------------------------------------------------------------------------------------")
for i in range(len(students)):
    print(f"{students[i]:12} | {Quiz1[i]:3}    | {Quiz2[i]:3}    | {Quiz3[i]:3}    | {finalExam[i]:5}   | {classParti[i]:8}            |   {Grades[i]:3} |  {Result[i]:3}")

       # Determine if each student has passed or failed and update the counters
        # Initialize counters for passed and failed students
passed_count = 0
failed_count = 0

# Iterate through the exam scores
for Score in Students:
    if result.upper() == "PASSED":
        passed_count +=1
    else:
        failed_count +1
# Print the results
print("============================================================================================")
print("Total passed students:", passed_count)
print("Total failed students:", failed_count)
print("============================================================================================")