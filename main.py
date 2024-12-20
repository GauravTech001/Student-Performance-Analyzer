student_records = {}

def add_student(student_id, marks):
    if student_id in student_records:
        print(f"Student ID {student_id} already exists.")
    else:
        student_records[student_id] = marks
        print(f"Student ID {student_id} added successfully.")

def update_student(student_id, marks):
    if student_id in student_records:
        student_records[student_id] = marks
        print(f"Student ID {student_id} updated successfully.")
    else:
        print(f"Student ID {student_id} does not exist.")

def delete_student(student_id):
    if student_id in student_records:
        del student_records[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print(f"Student ID {student_id} does not exist.")

def display_student_info(student_id):
    if student_id in student_records:
        marks = student_records[student_id]
        total_marks = sum(marks.values())
        percentage = {subject: (mark / total_marks) * 100 for subject, mark in marks.items()}
        
        print(f"\nStudent ID: {student_id}")
        print(f"Marks: {marks}")
        print(f"Total Marks: {total_marks}")
        print("Percentage in each subject:")
        for subject, percent in percentage.items():
            print(f"{subject}: {percent:.2f}%")
    else:
        print(f"Student ID {student_id} does not exist.")

def display_all_students():
    if not student_records:
        print("No student records available.")
        return
    for student_id in student_records:
        display_student_info(student_id)

def main():
    while True:
        print("\nStudent Records Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Student Info")
        print("5. Display All Students")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            marks = {}
            num_subjects = int(input("Enter number of subjects: "))
            for _ in range(num_subjects):
                subject = input("Enter subject name: ")
                mark = float(input(f"Enter marks for {subject}: "))
                marks[subject] = mark
            add_student(student_id, marks)

        elif choice == '2':
            student_id = input("Enter Student ID to update: ")
            marks = {}
            num_subjects = int(input("Enter number of subjects: "))
            for _ in range(num_subjects):
                subject = input("Enter subject name: ")
                mark = float(input(f"Enter marks for {subject}: "))
                marks[subject] = mark
            update_student(student_id, marks)

        elif choice == '3':
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)

        elif choice == '4':
            student_id = input("Enter Student ID to display info: ")
            display_student_info(student_id)

        elif choice == '5':
            display_all_students()

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()