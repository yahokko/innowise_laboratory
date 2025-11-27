def calc_average(student: dict):
    """
    Calculate the average grade for a student.
    
    Args:
        student (dict): A dictionary containing student's name and grades.
    
    Returns:
        float | None: Rounded average grade to 1 decimal place, or None if no grades.
    """
    if student['grades']:
        return round(sum(student['grades'])/len(student['grades']), 1)
    return None


def has_grades(students: list):
    """
    Check if at least one student has grades.
    
    Args:
        students (list): List of student dictionaries.

    Returns:
        bool: True if any student has grades, False otherwise.
    """
    return not all(not student['grades'] for student in students)



def is_students(students: list):
    """
    Check if the list of students is not empty.

    Args:
        students (list): List of students.

    Returns:
        bool: True if there are students, False otherwise.
    """
    return bool(students)


def is_student(name: str, students: list):
    """
    Check whether a student with a given name exists.

    Args:
        name (str): Student's name.
        students (list): List of student dictionaries.

    Returns:
        bool: True if the student exists, False otherwise.
    """
    return name in [student['name'] for student in students]


def add_student(name: str, students: list):
    """
    Add a new student to the list if they are not already present.

    Args:
        name (str): Student's name.
        students (list): List of students.
    """
    if not is_student(name, students):
        students.append({'name': name, 'grades' : []})
    else:
        print(f"The student '{name}' is already in the list.")


def add_grade(name:str, grade: int, students: list):
    """
    Add a grade to the specified student.

    Args:
        name (str): Student name.
        grade (int): Grade value from 0 to 100.
        students (list): List of students.
    """
    for student in students:
        if student['name'] == name:
            student['grades'].append(grade)


def stud_with_grades(students: list):
    """
    Filter students who have at least one grade.

    Args:
        students (list): List of students.

    Returns:
        list: Students with non-empty grade lists.
    """
    return [student for student in students if student['grades']]


def show_report(students: list):
    """
    Display a full report showing:
      - each student's average grade
      - min/max average among all students with grades
      - overall average of all grades
    
    Args:
        students (list): List of students.
    """
    print("--- Student Report ---")

    if not is_students(students):
        print('There are no students yet.')
        return
    
    max_avg = None
    min_avg = None
    overall_sum = 0

    # Show each student’s individual average
    for student in students:
        avg_grade = calc_average(student)

        # Track only valid averages
        if avg_grade is not None:
            overall_sum += avg_grade

            if min_avg == None or avg_grade < min_avg:
                min_avg = avg_grade
            if max_avg == None or avg_grade > max_avg:
                max_avg = avg_grade

        print(f"{student['name']}'s average grade is {'N/A' if avg_grade is None else avg_grade}")

    if not has_grades(students):
        print('There are no grades yet.')
        return
    
    # Final summary
    print(
        f"Max Average: {max_avg}\n"
        f"Min Average: {min_avg}\n"
        f"Overall Average: {overall_sum/len(stud_with_grades(students)):.1f}"
        )


def top_performer(students: list):
    """
    Identify and display the student with the highest average grade.
    
    Args:
        students (list): List of student dictionaries.
    """
    if not is_students(students):
        print('There are no students yet.')
        return
    
    elif not has_grades(students):
        print('There are no grades yet.')
        return
    
    valid_students = stud_with_grades(students)
    top_perf = max(valid_students, key=lambda x: calc_average(x))

    print(
        f"The student with the highest average is {top_perf['name']} "
        f"with a grade of {calc_average(top_perf)}"
        )


def main():
    """
    Entry point for the student grade analyzer program.
    Handles menu display and user interaction.
    """
    students = []

    while True:
        print(
            f"\n--- Student Grade Analyzer ---\n"
            f"1. Add a new student\n"
            f"2. Add grades for a student\n"
            f"3. Generate a full report\n"
            f"4. Find the top student\n"
            f"5. Exit program\n"
            )
        
        user_choice = input('Enter your choice: ').strip()

        if user_choice == '5':
            print("Exiting program.")
            break

        # Add student
        elif user_choice == '1':
            stud_name = ' '.join(input("Enter student name: ").title().split())

            # Validate
            if not stud_name.replace(' ', '').isalpha():
                print('Invalid input. Only letters are allowed')
            elif len(stud_name) < 2:
                print('Invalid input. Name must consist of minimum 2 letters')
            else:
                add_student(stud_name, students)

        # Add grade
        elif user_choice == '2':
            stud_name = ' '.join(input("Enter student name: ").title().split())

            if is_student(stud_name, students):
                while True:
                    grade_input = input("Enter a grade (or 'done' to finish): ").strip()

                    if grade_input.lower() == 'done':
                        break

                    try:
                        grade = int(grade_input)
                    except ValueError:
                        print('Invalid input. Please enter a number.')
                        continue

                    if  grade < 0 or grade > 100:
                        print("The grade cannot be lower than 0 or greater than 100")
                        continue

                    add_grade(stud_name, grade, students)

            else:
                print(f"The student '{stud_name}' is not in the list.")

        # Show full report
        elif user_choice == '3':
            show_report(students)

        # Top performer
        elif user_choice == '4':
            top_performer(students)


if __name__ == "__main__":
    main()