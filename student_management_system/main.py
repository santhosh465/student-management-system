from database import (
    create_database,
    add_student,
    get_all_students,
    update_student,
    delete_student
)

def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def main():
    create_database()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        # OPTION 1: ADD STUDENT
        if choice == "1":
            name = input("Enter student name: ").strip()
            email = input("Enter student email: ").strip()
            course = input("Enter course: ").strip()
            year_input = input("Enter year: ").strip()

            if not name or not email or not course or not year_input:
                print("All fields are required.")
                continue

            if not year_input.isdigit():
                print("Year must be a number.")
                continue

            year = int(year_input)
            add_student(name, email, course, year)
            print("Student added successfully!")

        # OPTION 2: VIEW STUDENTS
        elif choice == "2":
            students = get_all_students()

            if not students:
                print("No students found.")
            else:
                print("\n--- Student List ---")
                for student in students:
                    print(student)

        # OPTION 3: UPDATE STUDENT
        elif choice == "3":
            student_id_input = input("Enter student ID to update: ").strip()

            if not student_id_input.isdigit():
                print("Invalid ID.")
                continue

            student_id = int(student_id_input)

            name = input("New name: ").strip()
            email = input("New email: ").strip()
            course = input("New course: ").strip()
            year_input = input("New year: ").strip()

            if not name or not email or not course or not year_input:
                print("All fields are required.")
                continue

            if not year_input.isdigit():
                print("Year must be a number.")
                continue

            year = int(year_input)
            update_student(student_id, name, email, course, year)
            print("Student updated successfully!")

        # OPTION 4: DELETE STUDENT
        elif choice == "4":
            student_id_input = input("Enter student ID to delete: ").strip()

            if not student_id_input.isdigit():
                print("Invalid ID.")
                continue

            student_id = int(student_id_input)
            delete_student(student_id)
            print("Student deleted successfully!")

        # OPTION 5: EXIT
        elif choice == "5":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 

