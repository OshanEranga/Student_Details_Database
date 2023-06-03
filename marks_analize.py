
student_details = []

# Display Menu
def display_menu():
    print("Student Details Database")
    print()
    print("Menu")
    print()
    print("1 - Add New Student ")
    print("2 - Getting details of a student")
    print("3 - By getting details of all students")
    print("4 - Entering marks separately for each term")
    print("5 - Finding able to  who has the maximum average marks for a given term")
    print("6 - Who has the lowest marks in science?")
    print("7 - Delete student details")
    print("8 - Exit yhe program")
    print()

# Add new student
def add_new_student():
    stu_name = input("Please enter your name : ")
    stu_grade = input("Please enter your grade : ")
    stu_class = input("Please enter your class : ")
    stu_id = input("Please enter your student id : ")
    stu_details = (stu_id,stu_name,stu_grade,stu_class,"Not included",
                   "Not included","Not included","Not included","Not included",
                   "Not included","Not included","Not included","Not included")
    student_details.append(stu_details)
    print()
    print(f"Student Id of {stu_id} student entered.")
    print()

# Getting details of a student
def get_stu_details():
    if student_details != []:
        while True:
            stu_id = input("Please enter your student id : ")
            index = 4
            for x in student_details:
                if stu_id == x[0]:
                    print()
                    print("Student Details")
                    print()
                    print(f"Student Id : {x[0]}")
                    print(f"Student Name : {x[1]}")
                    print(f"Student grade : {x[2]}")
                    print(f"Student class : {x[3]}")
                    print()
                    print("Marks")
                    print()
                    for y in ["first","secound","third"]:
                        for z in ["Maths","Science","Art"]:
                            print(f"{y} term {z} : {x[index]}")
                            index += 1
                        print()
                    break
            if index == 4:
                print("Invalid Input.Enter Student Id again.")
                continue
            else:
                break

    else:
        print("No Student Details in database.")
        print()

# By getting details of all students
def get_all_stu_details():
    if student_details != []:
        num = 1
        print("Details in all students")
        print()
        for x in student_details:
                print()
                print(f"{num} Student Details")
                print()
                print(f"Student Id : {x[0]}")
                print(f"Student Name : {x[1]}")
                print(f"Student grade : {x[2]}")
                print(f"Student class : {x[3]}")
                print()
                print("Marks")
                print()
                index = 4
                for y in ["first","secound","third"]:
                    for z in ["Maths","Science","Art"]:
                        print(f"{y} term {z} : {x[index]}")
                        index += 1
                    print()
                if len(student_details) > num:
                    print("Next Student")
                    num +=1
                else:
                    if num == 1:
                        print(f"Show details in {num} student." )
                        print()
                    else:
                        print(f"Show details in {num} students." )
                        print()
    else:
        print("No Student Details in database.")
        print()



# Entering marks separately for each term
def entering_marks():
    if student_details != []:
        while True:
            stu_id = input("Please enter your student id : ")
            print()
            stu_index = 0
            index = 4
            for z in student_details:
                if stu_id == z[0]:
                    print("Please enter your marks")
                    print()
                    z_list = list(z)
                    for x in ["first","secound","third"]:    
                        for y in ["Maths","Science","Art"]:
                            while True:
                                marks = (input(f"{x} term {y} : "))
                                if 0 <= int(marks) and int(marks) <= 100:
                                    break
                                else:
                                    print("Invalid Input.Enter Marks again.")
                                    continue
                            
                            z_list[index] = marks
                            index +=1
                        print()
                    z_tuple = tuple(z_list)
                    student_details[stu_index] = z_tuple
                    break
                stu_index += 1     
            if index == 4:
                print("Invalid Input.Enter Student Id again.")
                continue
            else:
                print("Entering marks successfully.")
                break
    else:
        print("No Student Details in database.")
        print()

# Calculate average in list
def average(list : list) ->float:
    count = 0
    total = 0
    for num in list:
        total += num
        count += 1
    return total/count

# Finding able to  who has the maximum average marks for a given term
def find_term_max_average_students_id(term : int) ->list|float:
    max_average_students = []
    num = (term*3) + 1
    stu_id_and_ave = {}
    for x in student_details:
        marks_list = []
        for y in range(num,num +3):
            marks_list.append(int(x[y]))
        marks_average = average(marks_list)
        stu_id_and_ave[x[0]] = marks_average
    max_average = max(stu_id_and_ave.values())
    for key,value in stu_id_and_ave.items():
        if value == max_average:
            max_average_students.append(key)

    return max_average_students,max_average

# Finding able to Who has the lowest marks in science?
def find_lowest_marks_science_students_id(term : int) ->list | int:
    min_marks_students = []
    num = (term*3) + 2
    id_and_marks = {}
    for x in student_details:
        id_and_marks[x[0]] = int(x[num])
    marks_min = min(id_and_marks.values())
    for key,value in id_and_marks.items():
        if value == marks_min:
            min_marks_students.append(key)
    
    return min_marks_students,marks_min

# Delete student detail
def delete_details():
    stu_id = input("Enter student id for delete : ") 
    print()
    index = 0
    for x in student_details:
        if stu_id == x[0]:
            student_details.pop(index)
            break
        index += 1
    print(f"Id of {stu_id} student details deleted.")
    print()



while True:
    display_menu()
    choice = int(input("Please enter your choice : "))
    print()
    if choice == 1:
        add_new_student()
    elif choice == 2:
        get_stu_details()
    elif choice == 3:
        get_all_stu_details()
    elif choice == 4:
        entering_marks()
        print()
    elif choice == 5:
        while True:
            term = int(input("Enter the term number(1/2/3) : "))
            print()
            if term == 1 or term == 2 or term == 3:
                max_students_id_list , max_average = find_term_max_average_students_id(term)
                print("Maximum average marks Students")
                print()
                print("Student Id | Student Name")
                print()
                for k in student_details:
                    for j in max_students_id_list:
                        if k[0] == j:
                            print(f"{j} | {k[1]}")
                print()
                print(f"Maximum average is {round(max_average,2)}.")
                print()
                break

            else:
                print("Invalid input.Please re-enter the term number.")
                print()
                continue
    elif choice == 6:
            while True:
                term = int(input("Enter the term number(1/2/3) : "))
                print()    
                if term == 1 or term == 2 or term == 3:
                    min_science_students_id_list,loweest_marks = find_lowest_marks_science_students_id(term)
                    print("lowest marks in science Students") 
                    print()
                    print("Student Id | Student Name")
                    print()
                    for k in student_details:
                        for j in min_science_students_id_list:
                            if k[0] == j:
                                print(f"{j} | {k[1]}")

                    print()
                    print(f"Lowest marks in science is {loweest_marks}.")
                    print()
                    break

                else:
                    print("Invalid input.Please re-enter the term number.")
                    print()
                    continue         

    elif choice == 7:
        delete_details()

    elif choice == 8:
        print("Exit program.")
        break
    else:
        print("Invalid Input.Try again")
        print()
        continue

    