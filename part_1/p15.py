import datetime

FILENAME = "reservations.txt"


def reserve_ticket():
    try:
        pid = int(input("Enter Passenger ID: "))
        name = input("Enter Name: ")
        source = input("Enter Source: ")
        destination = input("Enter Destination: ")
        date = input("Enter Travel Date (YYYY-MM-DD): ")

        with open(FILENAME, 'a') as file:
            file.write(f"{pid},{name},{source},{destination},{date}\n")

        print("Ticket reserved successfully!")

    except ValueError:
        print("Invalid input! Passenger ID must be a number.")


def list_today_reservations():

    today = str(datetime.date.today())
    found = False

    try:
        with open(FILENAME, 'r') as file:

            print(f"\nReservations for today ({today}):")

            for line in file:

                data = line.strip().split(',')

                if len(data) != 5:
                    continue

                if data[4] == today:
                    print(
                        f"ID: {data[0]}, "
                        f"Name: {data[1]}, "
                        f"From: {data[2]}, "
                        f"To: {data[3]}"
                    )
                    found = True

        if not found:
            print("No reservations found for today.")

    except FileNotFoundError:
        print("No reservation file found!")

while True:

    print("\n--- Railway Reservation System ---")
    print("1. Reserve Ticket")
    print("2. List Today's Reservations")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        reserve_ticket()

    elif choice == '2':
        list_today_reservations()

    elif choice == '3':
        print("Exiting system...")
        break

    else:
        print("Invalid choice! Please try again.")