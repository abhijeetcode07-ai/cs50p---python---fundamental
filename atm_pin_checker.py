def atm():

    balance = 1000   # state outside loop

    while True:

        print("\n1 Balance")
        print("2 Deposit")
        print("3 Withdraw")
        print("4 Exit")

        command = input("Enter choice: ")

        if command == "1":
            print("Balance:", balance)

        elif command == "2":
            amount = int(input("Deposit amount: "))
            balance += amount

        elif command == "3":
            amount = int(input("Withdraw amount: "))
            if amount > balance:
                print("Insufficient funds")
            else:
                balance -= amount

        elif command == "4":
            print("Exited")
            break

        else:
            print("Invalid choice")


atm()