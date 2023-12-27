import random
import time
from os import system, name


def clear():
    """This function will be used to clear the screen"""
    if name == 'nt':  # Windows
        system('cls')
    else:  # Unix/Linux/macOS
        system('clear')

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

class Cash:
    def __init__(self, credit=200, bet=2):
        self.credit = credit
        self.bet = bet
        self.bets = [2, 5, 10, 20]
        self.bet_stack = Stack()

    def change_bet(self):
        self.bets.append(self.bets.pop(0))
        self.bet = self.bets[0]
        self.bet_stack.push(self.bet)

    def undo_bet(self):
        last_bet = self.bet_stack.pop()
        if last_bet is not None:
            self.bet = last_bet

    def charge(self):
        if self.bet <= self.credit:
            self.credit -= self.bet
            return False
        else:
            print('\n\t     Not enough credit to place a bet press "a" to add money!')
            time.sleep(1)
            return True

class SlotMachine:
    def __init__(self, slot_one, slot_two, slot_three):
        self.reels = [slot_one, slot_two, slot_three]
        self.loss_count = 0  # Add a counter for losses

    def spin(self):
        if  self.loss_count >= random.randint(3,7):
            # If there have been 3 in 7 losses, force a win by choosing the same symbol for all reels
            symbol = random.choices(self.reels[0], k=1)[0]
            return [symbol, symbol, symbol]
        else:
            # Otherwise, spin normally
            return [random.choices(reel, k=1)[0] for reel in self.reels]

    def print_loop_layout(self):
        result = self.spin()
        
        layout = ('\n\t   __________________________________________\n'
                '\t  /                                         /|\n'
                '\t /_________________________________________/ |\n'
                '\t|                                         |  |\n'
                '\t| STRAWBERRY x2  PLUM   x3   RASPBERRY x5 |  |\n'
                '\t| ORANGE     x8  BANANA x10  SEVENS   x15 |  |\n'
                '\t|                                         |  |\n'
                '\t|   -----------------------------------   |  |\n'
                f'\t|  |             {" ".join([res[0] for res in result])}              |  |  |\n'
                '\t|   -----------------------------------   |  |\n'
                '\t|                                         |  |\n'
                f'\t|   TOAL BET {cash.bet}               CREDIT {cash.credit} \n'
                '\t|                                         |  |\n'
                '\t|                Spining...               | /\n'
                '\t|_________________________________________|/')
        
        print(layout)

    def play(self, cash):
        clear()
        result = self.spin()
        
        layout = ('\n\t   __________________________________________\n'
                '\t  /                                         /|\n'
                '\t /_________________________________________/ |\n'
                '\t|                                         |  |\n'
                '\t| STRAWBERRY x2  PLUM   x3   RASPBERRY x5 |  |\n'
                '\t| ORANGE     x8  BANANA x10  SEVENS   x15 |  |\n'
                '\t|                                         |  |\n'
                '\t|   -----------------------------------   |  |\n'
                f'\t|  |             {" ".join([res[0] for res in result])}              |  |  |\n'
                '\t|   -----------------------------------   |  |\n'
                '\t|                                         |  |\n'
                f'\t|   TOAL BET {cash.bet}               CREDIT {cash.credit} \n'
                '\t|                                         |  |'
                )
        
        print(layout)
        
        if len(set([res[0] for res in result])) == 1:
            symbol = result[0][0]
            multiplier = result[0][1]
            win_amount = cash.bet * multiplier  # Calculate win amount based on bet and multiplier
            print(f"\t|     Congratulations! You won ${win_amount}!        | |")
            cash.credit += win_amount
            self.loss_count = 0  # Reset the loss counter after a win
        else:
            print("\t|      Sorry, you lost. Try again!        | /")
            self.loss_count += 1  # Increment the loss counter after a loss
        print('\t|_________________________________________|/')


# Define the symbols and multipliers
strawberry = ("🍓", 2)
banana = ("🍌", 10)
plum = ("🍑", 3)
raspberry = ("🍇", 5)
orange = ("🍊", 8)
seven = ("💎", 15)

# Define the probabilities for each symbol
probabilities = [13, 8, 6, 4, 3, 0.5]
symbols = [strawberry, plum, raspberry, orange, banana, seven]
slot_one = random.choices(symbols, weights=probabilities, k=100)

probabilities = [10, 6, 5, 3, 2, 0.5]
symbols = [strawberry, plum, raspberry, orange, banana, seven]
slot_two = random.choices(symbols, weights=probabilities, k=100)

probabilities = [10, 6, 5, 3, 2, 0.5]
symbols = [strawberry, plum, raspberry, orange, banana, seven]
slot_three = random.choices(symbols, weights=probabilities, k=100)

# Create a slot machine and cash with these symbols
slot_machine = SlotMachine(slot_one, slot_two, slot_three)
cash = Cash()

def welcome():
    welcome = ['\n\n\t #######    #######    #######',
               '\t########   ########   ########',
               '\t     ##         ##         ##',
               '\t    ##         ##         ##',
               '\t   ##         ##         ##',
               '\t  ##         ##         ##',
               '\t  ##         ##         ##',
               '\n\n'
               '\t  ##### ##    ####### ###### ',
               '\t  ##    ##    ##   ##   ##   ',
               '\t  ##### ##    ##   ##   ##   ',
               '\t     ## ##    ##   ##   ##   ',
               '\t  ##### ##### #######   ##   ']
    
    for c in welcome:
        print(c)
        time.sleep(0.1)
    time.sleep(1)
    clear()

def layout(): 
    print('\n\t   __________________________________________')
    print('\t  /                                         /|')
    print('\t /_________________________________________/ |')
    print(
                '\t|                                         |  |\n'
                '\t| STRAWBERRY x2  PLUM   x3   RASPBERRY x5 |  |\n'
                '\t| ORANGE     x8  BANANA x10  SEVENS   x15 |  |\n'
                '\t|                                         |  |\n'
                '\t|   -----------------------------------   |  |\n'
                f'\t|  |      WELCOME TO SLOT MACHINE      |  |  |\n'
                '\t|   -----------------------------------   |  |\n'
                '\t|                                         |  |\n'
                f'\t|   TOAL BET {cash.bet}               CREDIT {cash.credit}   \n'
                '\t|                                         |  |\n'
                '\t|                                         | /\n'
                '\t|_________________________________________|/'
        )

if __name__ == '__main__':
    clear()
    #welcome()
    layout()
    while True:
        """print(f"\nCurrent Bet: {cash.bet}, Current Credit: {cash.credit}")"""
        again = input("\nPress 'q' to quit\n      'b' to change bet \n      'a' to add money \nPress other key to spin: ")
        if again == 'q':
            break
        elif again == 'b':
            cash.change_bet()
            clear()
            layout()
        elif again == 'a':
            amount = int(input("Enter the amount of money you want to add: "))
            cash.credit += amount
            print(f"You added ${amount}. Your new credit is ${cash.credit}.")
            time.sleep(1)
            clear()
            layout()
        else:
            if not cash.charge():
                clear()
                """for i in range(6):
                    slot_machine.print_loop_layout()
                    time.sleep(0.1)
                    clear()
                for i in range(4):
                    slot_machine.print_loop_layout()
                    time.sleep(0.3)
                    clear()
                for i in range(3):
                    slot_machine.print_loop_layout()
                    time.sleep(0.5)
                    clear()
                for i in range(1):
                    slot_machine.print_loop_layout()
                    time.sleep(0.7)
                    clear()
                for i in range(2):
                    slot_machine.print_loop_layout()
                    time.sleep(0.8)
                    clear()"""        
                slot_machine.play(cash)
                
    time.sleep(1)
    clear()
    
""" 

? C lang maybe from OS?

    int child_pid = fork();
    if (child_pid == 0) {
        // Child process
        printf("Child process\n", getpid());
        return 0;
    } else {
        // Parent process
        printf("Parent process\n", child_pid());
        return 0;
    }"""