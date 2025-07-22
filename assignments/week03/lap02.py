# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print(f"your balance is: ${balance: .2f}")
        elif choice == "2":
            amount = float(input("Enter amount withdown:"))
            if amount <= balance:
                balance -= amount
                print(f"${amount : .2f}withdrown successfully.")
                print(f"New balance: ${balance: .2f}")
            else:
                print("Insufficient balance.")
        elif choice =="3":
            amount = float(input("Enter amount deposit: "))
            if amount > 0:
                balance += amount
                print(f"${amount:.2f} deposited successfully.")
                print(f"New balance: ${balance:.2f}")
            else:
                print("Invalid deposit amount.")
        elif choice == "4":
            print("Thank you for use ATM.")
            break
        else:
            print("Not this option try again")
else:
    print("Invalid PIN")