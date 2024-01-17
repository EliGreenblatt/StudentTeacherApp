import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, db
import os

class HomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Home Screen")

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "Images", "background.png")

        self.b_img = tk.PhotoImage(file=image_path)

        b_label = tk.Label(root, image=self.b_img)
        b_label.place(relwidth=1, relheight=1)

        login_b = tk.Button(root, text="Login", command=self.open_login_page, width=13, height=2)
        login_b.place(x=150, y=280)

        register_b = tk.Button(root, text="Register", command=self.register_click, width=13, height=2)
        register_b.place(x=150, y=320)

        window_width = 400
        window_height = 500
        self.root.geometry(f"{window_width}x{window_height}")

        # Initialize Firebase Admin SDK
        cred = credentials.Certificate(r"C:\Users\97252\Desktop\app_project\StudentTeacherApp\DataBase\studentapp-ba43c-firebase-adminsdk-ccgtn-7850f0df38.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://studentapp-ba43c-default-rtdb.firebaseio.com/'
        })

    def open_login_page(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("Login Page")

        username_label = tk.Label(login_window, text="Username:")
        username_label.pack()

        username_entry = tk.Entry(login_window)
        username_entry.pack()

            
        login_button = tk.Button(login_window, text="Login", command=lambda: self.perform_login(username_entry.get()))
        login_button.pack()

    def perform_login(self, username):
        # Query the database to check if the entered username and password exist
        users_ref = db.reference('students')  # Assuming 'students' is the correct path
        query = users_ref.order_by_child('name').equal_to(username).get()

        if query:
            for key, value in query.items():
                # Check the password if needed
                # if value['password'] == password:
                messagebox.showinfo("Login", "Login Successful!")
        else:
            messagebox.showerror("Login Failed", "User not found")

    def register_click(self):
        self.role_selection_window = tk.Toplevel(self.root)
        self.role_selection_window.title("Select Role")

        student_button = tk.Button(self.role_selection_window, text="Student", command=lambda: self.open_registration_window("student"))
        student_button.pack()

        teacher_button = tk.Button(self.role_selection_window, text="Teacher", command=lambda: self.open_registration_window("teacher"))
        teacher_button.pack()

        self.role_selection_window.mainloop()  # Start the event loop for the Toplevel window

    def open_registration_window(self, role):
        self.registration_window = tk.Toplevel(self.root)
        self.registration_window.title(f"Register as {role.title()}")

        name_label = tk.Label(self.registration_window, text="Name:")
        name_label.pack()
        self.name_entry = tk.Entry(self.registration_window)
        self.name_entry.pack()

        email_label = tk.Label(self.registration_window, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(self.registration_window)
        self.email_entry.pack()

        # Entry for age (for students) or subject (for teachers)
        if role == "student":
            age_label = tk.Label(self.registration_window, text="Age:")
            age_label.pack()
            self.age_entry = tk.Entry(self.registration_window)
            self.age_entry.pack()
        elif role == "teacher":
            subject_label = tk.Label(self.registration_window, text="Subject:")
            subject_label.pack()
            self.subject_entry = tk.Entry(self.registration_window)
            self.subject_entry.pack()

        register_button = tk.Button(self.registration_window, text="Register", command=lambda: self.register_user(role))
        register_button.pack()

    def register_user(self, role):
        name = self.name_entry.get()
        email = self.email_entry.get()

        if role == "student":
            age = self.age_entry.get()
            # Perform validation and Firebase registration for student
            users_ref = db.reference(role)  # Assuming 'students' is the correct path
            user_id = users_ref.push().key
            users_ref.child(user_id).set({
                'name': name,
                'email': email,
                'age': age
                # ...other fields
            })
        elif role == "teacher":
            subject = self.subject_entry.get()
            # Perform validation and Firebase registration for teacher
            users_ref = db.reference("teachers")  # Assuming 'teachers' is the correct path
            user_id = users_ref.push().key
            users_ref.child(user_id).set({
                'name': name,
                'email': email,
                'subject': subject
                # ...other fields
            })

        messagebox.showinfo("Registration Successful", "You have registered successfully!")
        self.registration_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeScreen(root)
    root.mainloop()
