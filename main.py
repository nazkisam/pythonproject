def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"Deposit successful: ${amount}")  # Debugging line
                return amount
            else:
                print('Amount must be positive.')
        else:
            print('Please enter a number.')

# Call the function
deposit()
