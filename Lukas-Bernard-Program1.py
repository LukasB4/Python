# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Lukas Bernard
# Last Modified: Sept 9, 2020 
# ---------------------------------------
# This program is used to calculate a gpa
# based on inputs from the user
# ---------------------------------------

# This is the main function: It gets user input for number of courses,
# grade in the course, and how many credits the course is worth.
# It outputs the users GPA

def main():
    uinput = int(input('Enter the number of courses you are taking: '))
    print()
    classnumber = 1
    overallcredit = 0
    overallgpa = 0.0
    while classnumber <= uinput:
        grade = input('Enter grade for course %d: ' %classnumber)
        credit = int(input('Enter credits for course %d: ' %classnumber))
        print()
        gradepoints = translate(grade)
        overallgpa = overallgpa + (credit * gradepoints)
        overallcredit += credit
        classnumber += 1
    
    overallgpa = overallgpa / overallcredit
    print('Your GPA is %.2f' %overallgpa)

# This translate function converts the letter grade into a usable number

def translate(grade):

    if (grade == 'A' or grade == 'a'):
        gradenum = 4.0  
    elif (grade == 'A-' or grade == 'a-'):
        gradenum = 3.7
    elif (grade == 'B+' or grade == 'b+'):
        gradenum = 3.3
    elif (grade == 'B' or grade == 'b'):
        gradenum = 3.0
    elif (grade == 'B-' or grade == 'b-'):
        gradenum = 2.7
    elif (grade == 'C+' or grade == 'c+'):
        gradenum = 2.3
    elif (grade == 'C' or grade == 'c'):
        gradenum = 2.0
    elif (grade == 'C-' or grade == 'c-'):
        gradenum = 1.7
    elif (grade == 'D+' or grade == 'd+'):
        gradenum = 1.3
    elif (grade == 'D' or grade == 'd'):
        gradenum = 1.0
    elif (grade == 'F' or grade == 'f'):
        gradenum = 0.0
        
    return gradenum
    
# This is where the main function is called

main()
