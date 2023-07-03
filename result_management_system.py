import mysql.connector

db = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "results")
cursor = db.cursor(buffered = True)

def section_1(enrolment_number_1):
    cursor.execute(f"SELECT student_name, fathers_name, mothers_name, roll_number, semester_number, spi_1, spi_2, spi_3, spi_4, spi_5 FROM students WHERE enrolment_number = {enrolment_number_1};")
    for row in cursor:
        return [row[0], row[1], row[2], row[3], row[4], [row[5], row[6], row[7], row[8], row[9]], f"Name: {row[0]}\nFather's Name: {row[1]}\nMother's Name: {row[2]}\nEnrolment Number: {enrolment_number_1}\nRoll Number: {row[3]}\nSemester {row[4]}"]

def section_2(enrolment_number_1):
    cursor.execute(f"SELECT course_name, branches.branch_name FROM branches INNER JOIN students ON branches.branch_code = students.branch_code WHERE enrolment_number = {enrolment_number_1};")
    for row in cursor:
        return [row[0], row[1], f"Course: {row[0]}\nBranch: {row[1]}"]

def section_3(enrolment_number_1):
    cursor.execute(f"SELECT DISTINCT enrolment_number, subjects.subject_code, subject_name, grade_point, credits FROM subjects INNER JOIN grade_points ON subjects.subject_code = grade_points.subject_code WHERE enrolment_number = {enrolment_number_1};")
    subject_result_1 = []
    grade_points_1 = []
    credits_1 = []
    for row in cursor:
        subject_result_1.append(f"{row[1]} - {row[2]} - {row[3]} - {row[4]}")
        grade_points_1.append(row[3])
        credits_1.append(row[4])
    return [subject_result_1, grade_points_1, credits_1]

def result_calculator(grade_points_1):
    number_of_supply_subjects_1 = [True for i in grade_points_1 if i < 6].count(True)
    if 0 in grade_points_1 or number_of_supply_subjects_1 > 1:
        return "FAIL"
    elif number_of_supply_subjects_1 == 1:
        return "PASS BY GRACE"
    return "PASS"

def spi_calculator(result_1, grade_points_1, credits_1):
    if result_1 == "FAIL":
        return 0
    grade_points_1_times_credits_1_sum = 0
    credits_1_sum = 0
    for i in range(len(grade_points_1)):
        grade_points_1_times_credits_1_sum += grade_points_1[i]*credits_1[i]
        credits_1_sum += credits_1[i]
    return grade_points_1_times_credits_1_sum/credits_1_sum

def cpi_calculator(result_1, spis_1, semester_number_1, spi_1):
    cpi_1 = 0
    if result_1 != "FAIL" and 0 not in [spis_1[i] for i in range(semester_number_1 - 1)]:
        for i in range(semester_number_1 - 1):
            cpi_1 += spis_1[i]
        cpi_1 = (cpi_1 + spi_1)/semester_number_1
    return cpi_1

def attendance_calculator(enrolment_numbers_1):
    attendance_1 = len(enrolment_numbers_1)
    for i in enrolment_numbers_1:
        cursor.execute(f"SELECT grade_point FROM grade_points where enrolment_number = {i} AND grade_point = 0;")
        if cursor.rowcount != 0:
            attendance_1 -= 1
    return attendance_1

def number_of_results_calculator(enrolment_numbers_1, result_1):
    return [True for i in enrolment_numbers_1 if result_calculator(section_3(i)[1]) == result_1].count(True)

def headings_printer(enrolment_number_1):
    print(section_1(enrolment_number_1)[6])
    semester_number_1 = section_1(enrolment_number_1)[4]
    spis_1 = section_1(enrolment_number_1)[5]

    print(section_2(enrolment_number_1)[2])

    print("Subject Code - Subject Name - Grade Point - Credits:")
    for i in section_3(enrolment_number_1)[0]:
        print(i)
    grade_points_1 = section_3(enrolment_number_1)[1]
    credits_1 = section_3(enrolment_number_1)[2]

    result_1 = result_calculator(grade_points_1)
    print(f"Result: {result_1}")

    spi_1 = spi_calculator(result_1, grade_points_1, credits_1)
    print(f"SPI: {spi_1:.2f}")

    print(f"CPI: {cpi_calculator(result_1, spis_1, semester_number_1, spi_1):.2f}\n")

def analysis_printer(enrolment_numbers_1):
    attendance_1 = attendance_calculator(enrolment_numbers_1)
    print("Students:")
    print(f"present for all subjects = {attendance_1} ({attendance_1 * 100/len(enrolment_numbers_1):.2f}%)")
    print(f"absent for at least one subject = {len(enrolment_numbers_1) - attendance_1} ({(len(enrolment_numbers_1) - attendance_1) * 100/len(enrolment_numbers_1):.2f}%)\n")
    for i in ["FAIL", "PASS BY GRACE", "PASS"]:
        print(f"with the result {i} = {number_of_results_calculator(enrolment_numbers_1, i)} ({number_of_results_calculator(enrolment_numbers_1, i) * 100/len(enrolment_numbers_1):.2f}%)")
    print(f"\npassed the exams = {number_of_results_calculator(enrolment_numbers_1, 'PASS') + number_of_results_calculator(enrolment_numbers_1, 'PASS BY GRACE')} ({(number_of_results_calculator(enrolment_numbers_1, 'PASS') + number_of_results_calculator(enrolment_numbers_1, 'PASS BY GRACE')) * 100/len(enrolment_numbers_1):.2f}%)")
    print(f"failed the exams = {number_of_results_calculator(enrolment_numbers_1, 'FAIL')} ({number_of_results_calculator(enrolment_numbers_1, 'FAIL') * 100/len(enrolment_numbers_1):.2f}%)")
    print(f"Total number of students = {len(enrolment_numbers_1)}\n")

print("Select one option by entering its number for each prompt.")

while True:
    print("\n1 - view your result")
    print("2 - view the results of all students in a branch from a semester")
    print("3 - view the results of all students of the institute")
    print("4 - view enrolment numbers, names, SPIs, CPIs and results of all students of the institute")
    print("5 - enter an SQL SELECT statement")
    print("6 - enter any SQL statement")
    user_input = input("7 - stop\n")

    if user_input == "1":
        enrolment_number = input("Enter your enrolment number here - ")
        print("\nNational Institute of Technology Raipur\nSPRING 2020 EXAMINATION")
        headings_printer(enrolment_number)

    if user_input == "2":
        cursor.execute("SELECT branch_code FROM branches;")
        branch_codes = [row[0] for row in cursor]
        print("Select a branch from:")
        [print(f"{i + 1} - {branch_codes[i]}") for i in range(len(branch_codes))]
        selected_branch_code_number = int(input("Enter the number here - ")) - 1
        cursor.execute(f"SELECT DISTINCT semester_number FROM branches INNER JOIN students ON branches.branch_code = students.branch_code WHERE branches.branch_code = '{branch_codes[selected_branch_code_number]}' ORDER BY semester_number;")
        semester_numbers = [row[0] for row in cursor]
        if len(semester_numbers) > 1:
            print("Select a semester from:")
            [print(f"{i + 1} - Semester {semester_numbers[i]}") for i in range(len(semester_numbers))]
            selected_semester_number = semester_numbers[int(input("Enter the number here - ")) - 1]
        else:
            selected_semester_number = semester_numbers[0]
            print(f"The {branch_codes[selected_branch_code_number]} branch has students only in Semester {selected_semester_number}.")
        print(f"\nNational Institute of Technology Raipur\nSPRING 2020 EXAMINATION\n{branch_codes[selected_branch_code_number]} Branch Semester {selected_semester_number}\n")
        cursor.execute(f"SELECT enrolment_number FROM students WHERE branch_code = '{branch_codes[selected_branch_code_number]}' AND semester_number = {selected_semester_number};")

    if user_input == "3":
        cursor.execute("SELECT enrolment_number FROM students ORDER BY enrolment_number;")

    if user_input in ["2", "3"]:
        enrolment_numbers = [row[0] for row in cursor]
        [headings_printer(i) for i in enrolment_numbers]
        analysis_printer(enrolment_numbers)

    if user_input == "4":
        cursor.execute("SELECT enrolment_number from students ORDER BY enrolment_number;")
        print("")
        for i in [row[0] for row in cursor]:
            semester_number = section_1(i)[4]
            spis = section_1(i)[5]
            grade_points = section_3(i)[1]
            credits = section_3(i)[2]
            result = result_calculator(grade_points)
            spi = spi_calculator(result, grade_points, credits)
            cpi = cpi_calculator(result, spis, semester_number, spi)
            name = section_1(i)[0]
            print(f"{i} - {name} - {spi:.2f} - {cpi:.2f} - {result}")
        print("")

    if user_input == "5":
        cursor.execute("SELECT" + input("Refer to the image at https://github.com/konda-suraj/projects for the database. Enter the rest of the query:\nSELECT "))

    if user_input == "6":
        username = input("Enter your username here - ")
        password = input("Enter your password here - ")
        if username == "manager_username" and password == "manager_password":
            cursor.execute(input("Refer to the image at https://github.com/konda-suraj/projects for the database.\nEnter the query here - "))
            db.commit()

    if user_input in ["5", "6"]:
        [print(row) for row in cursor]
        print("")

    if user_input in ["1", "2", "3", "4", "5", "6"]:
        print("\n1 - start again")
        if input("2 - stop\n") == "2":
            break

    if user_input == "7":
        break
