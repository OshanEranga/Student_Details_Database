
student_details = []

# ANSI escape sequences for text colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'

# ANSI escape sequence for resetting text color
RESET = '\033[0m'

# Display Menu
def display_menu():
    print(f"{YELLOW}-------------------------------------------------------------------------{RESET}")
    print(f"{YELLOW}Student Details Database{RESET}\n")
    print(f"{CYAN}Menu{RESET}\n")
    print(f"{GREEN}1{RESET} - {MAGENTA}Add New Student{RESET} ")
    print(f"{GREEN}2{RESET} - {MAGENTA}Getting details of a student{RESET}")
    print(f"{GREEN}3{RESET} - {MAGENTA}By getting details of all students{RESET}")
    print(f"{GREEN}4{RESET} - {MAGENTA}Entering marks separately for each term{RESET}")
    print(f"{GREEN}5{RESET} - {MAGENTA}Finding able to  who has the maximum average marks for a given term{RESET}")
    print(f"{GREEN}6{RESET} - {MAGENTA}Who has the lowest marks in science?{RESET}")
    print(f"{GREEN}7{RESET} - {MAGENTA}Delete student details{RESET}")
    print(f"{GREEN}8{RESET} - {MAGENTA}Exit the program{RESET}")
    print(f"{YELLOW}-------------------------------------------------------------------------{RESET}")

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
    print(f"\n{GREEN}Student Id of{RESET} {YELLOW}{stu_id}{RESET} {GREEN}student entered.{RESET}")

# Getting details of a student
def get_stu_details():
    if student_details != []:
        while True:
            stu_id = input("Please enter your student id : ")
            index = 4
            print_details = False
            for x in student_details:
                if stu_id == x[0]:
                    print(f"\n{MAGENTA}Student Details{RESET}\n")
                    print(f"Student Id : {x[0]}")
                    print(f"Student Name : {x[1]}")
                    print(f"Student grade : {x[2]}")
                    print(f"Student class : {x[3]}")
                    print(f"\n{CYAN}Marks{RESET}\n")
                    for y in ["first","secound","third"]:
                        for z in ["Maths","Science","Art"]:
                            print(f"{y} term {z} : {x[index]}")
                            index += 1
                        print()
                    print_details = True
                    break
            if print_details:
                break
            else:
                print(f"\n{RED}Invalid Student Id Input.Enter Student Id again.{RESET}\n")
                continue

    else:
        print(f"\n{RED}No Student Details in database.{RESET}")

# By getting details of all students
def get_all_stu_details():
    if student_details != []:
        num = 1
        print(f"{CYAN}Details in all students{RESET}\n")
        for x in student_details:
                print(f"\n{MAGENTA}{num} Student Details{RESET}\n")
                print(f"Student Id : {x[0]}")
                print(f"Student Name : {x[1]}")
                print(f"Student grade : {x[2]}")
                print(f"Student class : {x[3]}")
                print(f"\n{CYAN}Marks{RESET}\n")
                index = 4
                for y in ["first","secound","third"]:
                    for z in ["Maths","Science","Art"]:
                        print(f"{y} term {z} : {x[index]}")
                        index += 1
                    print()
                if len(student_details) > num:
                    print(f"\n{BLUE}Next Student{RESET}")
                    num +=1
                else:
                    if num == 1:
                        print(f"\n{GREEN}Show details in {num} student.{RESET}")
                    else:
                        print(f"\n{GREEN}Show details in {num} students.{RESET}")
    else:
        print(f"\n{RED}No Student Details in database.{RESET}")



# Entering marks separately for each term
def entering_marks():
    if student_details != []:
        while True:
            stu_id = input("Please enter your student id : ")
            stu_index = 0
            index = 4
            marks_entered = False
            for z in student_details:
                if stu_id == z[0]:
                    print(f"\n{BLUE}Please enter your marks{RESET}\n")
                    z_list = list(z)
                    for x in ["first","secound","third"]:    
                        for y in ["Maths","Science","Art"]:
                            while True:
                                try:
                                    marks = int(input(f"{x} term {y} : "))
                                except ValueError:
                                    print(f"\n{RED}Invalid Marks Input.Enter Marks again.{RESET}\n")
                                    continue    
                                if 0 <= marks and marks <= 100:
                                    break
                                else:
                                    print(f"\n{RED}Invalid Marks Input.Enter Marks again.{RESET}\n")
                                    continue
                            
                            z_list[index] = marks
                            index +=1
                        print()
                    z_tuple = tuple(z_list)
                    student_details[stu_index] = z_tuple
                    marks_entered = True
                    break
                stu_index += 1     
            if marks_entered:
                print(F"\n{GREEN}Entering marks successfully.{RESET}")
                break
            else:
                print(f"\n{RED}Invalid Input.Enter Student Id again.{RESET}\n")
                continue
    else:
        print(f"\n{RED}No Student Details in database.{RESET}")
        

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
    if student_details != []:
        while True:
            stu_id = input("Enter student id for delete : ")
            delete = False
            index = 0
            for x in student_details:
                if stu_id == x[0]:
                    student_details.pop(index)
                    delete = True
                    break
                index += 1
            if delete:
                print(f"\n{GREEN}Id of{RESET} {YELLOW}{stu_id}{RESET} {GREEN}student details{RESET} {RED}deleted.{RESET}")
                break
            else:
                print(f"\n{RED}Invalid Student Id Input.Enter Student Id again.{RESET}\n")
                continue
    else:
        print(f"\n{RED}No Student Details in database for delete students details.{RESET}")



while True:
    display_menu()
    try:
        choice = int(input("Please enter your choice number : "))
    except ValueError:
        print(f"\n{RED}An invalid input(choice number) was entered.Re-enter a valid input(choice number).{RESET}\n")
        continue
    print(f"{YELLOW}-------------------------------------------------------------------------{RESET}")
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
            try:
                term = int(input("Enter the term number(1/2/3) : "))
            except ValueError:
                print(f"\n{RED}An invalid input(term number) was entered.Re-enter a valid input(term number).{RESET}\n")
                continue
                
            if term == 1 or term == 2 or term == 3:
                max_students_id_list , max_average = find_term_max_average_students_id(term)
                print(f"\n{MAGENTA}Maximum average marks Students{RESET}\n")
                print(f"{YELLOW}Student Id | Student Name{RESET}\n")
                for k in student_details:
                    for j in max_students_id_list:
                        if k[0] == j:
                            print(f"{j} | {k[1]}")
                print(f"\n{GREEN}Maximum average is {round(max_average,2)}.{RESET}")
                break

            else:
                print(f"\n{RED}Wroung term number.Please re-enter the term number.{RESET}\n")
                continue
    elif choice == 6:
            while True:
                try:
                    term = int(input("Enter the term number(1/2/3) : "))
                except ValueError:
                    print(f"\n{RED}An invalid input(term number) was entered.Re-enter a valid input(term number).{RESET}\n")
                    continue
                if term == 1 or term == 2 or term == 3:
                    min_science_students_id_list,loweest_marks = find_lowest_marks_science_students_id(term)
                    print(f"\n{MAGENTA}lowest marks in science Students{RESET}\n") 
                    print(f"{YELLOW}Student Id | Student Name{RESET}\n")
                    for k in student_details:
                        for j in min_science_students_id_list:
                            if k[0] == j:
                                print(f"{j} | {k[1]}")
                    print(f"\n{GREEN}Lowest marks in science is {loweest_marks}.{RESET}\n")
                    break

                else:
                    print(f"\n{RED}Wrong term number.Please re-enter the term number.{RESET}\n")
                    continue         

    elif choice == 7:
        delete_details()

    elif choice == 8:
        print(f"{BLUE}Exit program.{RESET}")
        break
    else:
        print(f"\n{RED}Wroung choice number.Please re-enter the choice number.{RESET}\n")
        continue

    