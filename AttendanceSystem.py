from datetime import date

class AttendanceSystem:
    def __init__(self, filename="attendance.txt"):
        self.records = {}
        self.filename = filename
        self.today = date.today()

    def mark_attendance(self):
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        status = input("Present / Absent: ").capitalize()

        if roll not in self.records:
            self.records[roll] = {
                "name": name,
                "present": 0,
                "total": 0
            }

        self.records[roll]["total"] += 1
        if status == "Present":
            self.records[roll]["present"] += 1

        print("Attendance marked for", self.today)

    def view_attendance(self):
        if not self.records:
            print("No records found")
            return

        print("\nRoll | Name | Present | Total | Percentage")
        for roll, data in self.records.items():
            percent = (data["present"] / data["total"]) * 100
            print(roll, "|", data["name"], "|",
                  data["present"], "|", data["total"],
                  "|", f"{percent:.2f}%")

    def save_to_file(self):
        with open(self.filename, "a") as file:
            file.write(f"\nDate: {self.today}\n")
            for roll, data in self.records.items():
                percent = (data["present"] / data["total"]) * 100
                file.write(
                    f"{roll},{data['name']},{data['present']},"
                    f"{data['total']},{percent:.2f}%\n"
                )
        print("Attendance saved to file")

# Main Program
system = AttendanceSystem()

while True:
    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Save to File")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.mark_attendance()
    elif choice == "2":
        system.view_attendance()
    elif choice == "3":
        system.save_to_file()
    elif choice == "4":
        print("Program Ended")
        break
    else:
        print("Invalid choice")
