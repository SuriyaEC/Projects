import csv
from datetime import datetime

def create_ticket():
    name = input("Enter user name: ")
    issue = input("Enter issue description: ")
    urgency = input("Enter urgency (High/Medium/Low): ")

    with open("tickets.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, issue, urgency])
        print("Ticket logged successfully!")

def view_tickets():
    try:
        with open("tickets.csv", mode="r") as file:
            reader = csv.reader(file)
            print("\n Existing Tickets:\n")
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print(" No tickets found.")

if __name__ == "__main__":
    while True:
        print("\n=== Ticket Logger ===")
        print("1. Log new ticket")
        print("2. View all tickets")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            break
        else:
            print(" Invalid choice.")