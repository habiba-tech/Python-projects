students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        students[roll] = name
        print("Student added")

    elif choice == "2":
        if students:
            print("\nStudent List:")
            for roll, name in students.items():
                print(roll, "-", name)
        else:
            print("No records found")

    elif choice == "3":
        roll = input("Enter Roll No to search: ")
        if roll in students:
            print("Student Name:", students[roll])
        else:
            print("Student not found")

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid choice")
