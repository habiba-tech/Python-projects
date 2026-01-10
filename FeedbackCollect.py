# Feedback Collection System - Python Mini Project

class FeedbackSystem:
    def __init__(self):
        self.feedbacks = []

    def add_feedback(self):
        name = input("Enter your name: ")
        rating = input("Enter rating (1 to 5): ")
        comment = input("Enter feedback: ")
        self.feedbacks.append({
            "Name": name,
            "Rating": rating,
            "Comment": comment
        })
        print("Feedback submitted")

    def view_feedbacks(self):
        if not self.feedbacks:
            print("No feedback available")
        else:
            print("\nCollected Feedbacks:")
            for i, f in enumerate(self.feedbacks, start=1):
                print(f"\n{i}. Name:", f["Name"])
                print("   Rating:", f["Rating"])
                print("   Comment:", f["Comment"])


# Main Program
system = FeedbackSystem()

while True:
    print("\n1. Submit Feedback")
    print("2. View Feedbacks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_feedback()
    elif choice == "2":
        system.view_feedbacks()
    elif choice == "3":
        print("Program Ended")
        break
    else:
        print("Invalid choice")
