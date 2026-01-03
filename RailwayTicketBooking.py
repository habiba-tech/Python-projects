# Railway Ticket Booking System (Basic)

class RailwayBooking:
    def __init__(self):
        self.tickets = {}
        self.ticket_no = 1000

    def book_ticket(self):
        name = input("Enter passenger name: ")
        source = input("Enter source station: ")
        destination = input("Enter destination station: ")
        seats = int(input("Enter number of seats: "))

        self.ticket_no += 1
        self.tickets[self.ticket_no] = {
            "Name": name,
            "From": source,
            "To": destination,
            "Seats": seats
        }

        print("Ticket booked successfully")
        print("Your Ticket Number is:", self.ticket_no)

    def view_ticket(self):
        tno = int(input("Enter ticket number: "))
        if tno in self.tickets:
            ticket = self.tickets[tno]
            print("\nPassenger Name:", ticket["Name"])
            print("From:", ticket["From"])
            print("To:", ticket["To"])
            print("Seats:", ticket["Seats"])
        else:
            print("Ticket not found")

    def cancel_ticket(self):
        tno = int(input("Enter ticket number to cancel: "))
        if tno in self.tickets:
            del self.tickets[tno]
            print("Ticket cancelled successfully")
        else:
            print("Ticket not found")


# Main Program
system = RailwayBooking()

while True:
    print("\n1. Book Ticket")
    print("2. View Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.book_ticket()
    elif choice == "2":
        system.view_ticket()
    elif choice == "3":
        system.cancel_ticket()
    elif choice == "4":
        print("Program Ended")
        break
    else:
        print("Invalid choice")
