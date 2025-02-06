import random

#global constant
MAX_LINES = 3
MAX_BET =100
MIN_BET = 1


ROWS = 3
COLS = 3

symbol_count = {
    "A" :2,
    "B" :4,
    "C" :6,
    "D" :8
}


def get_spin(rows,cols,symbols):
  all_symbols = []
  for symbol,symbol_count in symbols.items():
     for _ in range (symbol_count): #_ ananomous var
        all_symbols.append(symbol) 

  columns = []
  for _ in range (cols):
     column = []
     current_symbols = all_symbols[:]
     for _ in range (rows):         
         value = random.choice(all_symbols)      
         current_symbols.remove(value)
         column.append(value) 

     columns.append(column)
  return columns   

def print_slot_machine(columns):
    #transposing
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i !=len(columns) - 1:
             print(column[row], "|") 
            else:
             print(column[row]) 



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

def get_bet():
    while True:
        amount = input('What would you like to  bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                print(f"bet sucessfull: ${amount}")  # Debugging line
                return amount
            else: 
                print(f'Amount must be in range of ${MIN_BET} and ${MAX_BET}.')
        else:
            print('Please enter a positive number.')











def main():
    balance = deposit()
    lines = pick_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print('Not enough balance')
            break  # Exit if there isn't enough balance for this bet
        else:
            print(balance, lines, bet)
            print(f'You are betting {bet}$ on {lines} lines and total bet amount = {total_bet}')
            
            # Slot machine logic
            slot = get_spin(ROWS, COLS, symbol_count)
            print_slot_machine(slot)
            
            balance -= total_bet  # Deduct the bet from the balance

            # If balance is insufficient for the next round, end the game
            if balance < total_bet:
                print("Not enough balance for another round. Game over.")
                break

main()
