# Student Record Manager
# Python + SQL (IP Level Project)

import sqlite3

# connect to database (file ban jayegi)
conn = sqlite3.connect("students.db")
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    roll INTEGER,
    name TEXT,
    marks INTEGER
)
""")

conn.commit()

while True:
    print("\n--- STUDENT RECORD MANAGER ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        r = int(input("Enter Roll No: "))
        n = input("Enter Name: ")
        m = int(input("Enter Marks: "))

        cur.execute("INSERT INTO student VALUES (?, ?, ?)", (r, n, m))
        conn.commit()
        print("Student Added Successfully")

    elif choice == "2":
        cur.execute("SELECT * FROM student")
        data = cur.fetchall()

        print("\nRoll  Name   Marks")
        for i in data:
            print(i[0], " ", i[1], " ", i[2])

    elif choice == "3":
        r = int(input("Enter Roll No to Delete: "))
        cur.execute("DELETE FROM student WHERE roll = ?", (r,))
        conn.commit()
        print("Record Deleted")

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

conn.close()
