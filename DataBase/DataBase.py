import mysql.connector

# צור חיבור ל-MySQL
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='evyatar1q2w',
)

connection.create_database('StudentTeacherDB', ['my_app_user'])
