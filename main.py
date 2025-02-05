#global constant
MAX_LINES = 3



def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"Deposit successful: ${amount}")  # Debugging line
                return amount
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a positive number.')

# Call the function



def pick_number_of_lines():
       while True:
        lines = input('enter the number of lines you want to bet on (1-'+str(MAX_LINES)+')?')
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print('enter a valid number of lines.')
        else:
            print('enter a number')
       return lines


def main():
 balance = deposit()
 lines  = pick_number_of_lines()
 print(balance,lines)
 
main()
