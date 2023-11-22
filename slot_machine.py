import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

rows = 3
cols = 3

symbol_count = {"A":2,"B":2,"C":6,"D":8}

symbol_value={"A":5,"B":4,"C":3,"D":2}


def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] 
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
               break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)

    return winnings,winning_lines           

      

def get_slot_machine_spin(rows,cols,symbol):
    all_symbol = []
    for symbol,symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)
        print(all_symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns
    

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:    
                print(column[row],end="")


        print()              
    

def deposit():
    while True:
        amount = input("enter amount you want to deposit")
        if amount.isdigit:
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("please enter amount greater than zero")

        else:
            print("enter a digit")

    return amount

def get_number_of_lines():
    while True:
        lines = input("please enter number of lines(1- "  + str(MAX_LINES)+")?")
        if lines.isdigit:
           lines= int(lines)
           if 1<=lines<= MAX_LINES:
              break
           else:
               print("please enter a VALID NUMBER oF LINES")

        else:
            print("enter a digit")
        
    return lines
    

def get_bet():
    while True:
        amount = input("what would you like to bet on each line?")
        if amount.isdigit:
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("please enter amount between ${MIN_BET} and ${MAX_BET}")

        else:
            print("enter a digit")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
       bet = get_bet()
       total_bet = bet*lines 
       if total_bet > balance:
           print("you do not have enough balance to bet that amount , your current balance is: {balance} ")
       else:
           break    
    print(f"you are betting ${bet} on {lines} [lines. Total bet is equal to :${total_bet}" )

    slots = get_slot_machine_spin(rows,cols,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines    = check_winnings(slots,lines,bet,symbol_value)
    print(f"you won{winnings}.")
    print(f"you won on lines:", * winning_lines)
    return (winnings - total_bet)

    


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("press enter to spin(q to quit)")
        if answer == "q":
            break
        balance +=spin(balance)
print(f"you left with $(balance)")


   

main()    
