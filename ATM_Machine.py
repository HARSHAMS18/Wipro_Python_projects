correct_pin = "68420"
balance = 50000
attempts = 0

print("========================================")
print("       Welcome to ATM Machine")
print("========================================")

while attempts < 3:
    pin = input("Enter ATM PIN: ")

    if pin == correct_pin:
        print("Login Successful")

        while True:
            print("\n1: Check Balance")
            print("2: Withdraw Money")
            print("3: Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Your Balance:", balance)

            elif choice == 2:
                amount = int(input("Enter amount: "))
                if amount > balance:
                    print("Insufficient Balance")
                else:
                    balance -= amount
                    print("Remaining Balance:", balance)

            elif choice == 3:
                print("Thank you for using ATM")
                break

            else:
                print("Invalid Choice")

            again = input("Do you want another transaction? (yes/no): ")
            if again.lower() != "yes":
                print("Thank you for using ATM")
                break

        break

    else:
        attempts += 1
        print("Wrong PIN. Attempts left:", 3 - attempts)

if attempts == 3:
    print("Account Locked")

print("========================================")
