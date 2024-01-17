import firebase_admin
from firebase_admin import credentials, db

def add_student(cred):
    # Initialize Firebase Admin SDK
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://studentapp-ba43c-default-rtdb.firebaseio.com/'
    })

    # Reference to the 'students' node in the database
    students_ref = db.reference('students')

    # Get student details from user input
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    age = int(input("Enter student age: "))

    # Add student data to the database
    new_student_ref = students_ref.push({
        "name": name,
        "email": email,
        "age": age
    })

    print(f"Student '{name}' added successfully!")

def add_teacher():
    # Reference to the 'teachers' node in the database
    teachers_ref = db.reference('teachers')

    # Get teacher details from user input
    name = input("Enter teacher name: ")
    email = input("Enter teacher email: ")
    subject = input("Enter subject taught: ")

    # Add teacher data to the database
    new_teacher_ref = teachers_ref.push({
        "name": name,
        "email": email,
        "subject": subject
    })

    print(f"Teacher '{name}' added successfully!")

def search_database():
   

    print("Choose an option:")
    print("1. Search for a student")
    print("2. Search for a teacher")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        search_student()
    elif choice == '2':
        search_teacher()
    else:
        print("Invalid choice. Please enter 1 or 2.")

def search_student():
    # Reference to the 'students' node in the database
    students_ref = db.reference('students')

    # Get value to search for
    search_name = input("Enter the student name to search for: ")

    # Search for the value in the database
    query = students_ref.order_by_child('name').equal_to(search_name).get()

    if query:
        print("Results found for students:")
        for key, value in query.items():
            print(f"Key: {key}, Value: {value}")
    else:
        print("No results found for students.")

def search_teacher():
    # Reference to the 'teachers' node in the database
    teachers_ref = db.reference('teachers')

    # Get value to search for
    search_name = input("Enter the teacher name to search for: ")

    # Search for the value in the database
    query = teachers_ref.order_by_child('name').equal_to(search_name).get()

    if query:
        print("Results found for teachers:")
        for key, value in query.items():
            print(f"Key: {key}, Value: {value}")
    else:
        print("No results found for teachers.")

def main():
    cred = credentials.Certificate(r"C:\Users\97252\Desktop\app_project\StudentTeacherApp\DataBase\studentapp-ba43c-firebase-adminsdk-ccgtn-7850f0df38.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://studentapp-ba43c-default-rtdb.firebaseio.com/'
    })
    
    print("Choose an option:")
    print("1. Add a student")
    print("2. Add a teacher")
    print("3. Search in the database")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        add_student(cred)
    elif choice == '2':
        add_teacher()
    elif choice == '3':
        search_database()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
