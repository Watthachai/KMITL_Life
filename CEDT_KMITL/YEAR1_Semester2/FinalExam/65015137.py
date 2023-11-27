class Coffee:
    def __init__(self, name, water, milk, coffee, cost, total):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost
        self.total = total

        if self.name == 'latte' and self.total >= 75:
            self.water -= 200
            self.milk -= 150
            self.coffee -= 25
            self.total -= self.cost
            print(f'Here is {self.total} baht in change.')
        elif self.name == 'espresso' and self.total >= 50:
            self.water -= 50
            self.milk -= 0
            self.coffee -= 18
            self.total -= self.cost
            print(f'Here is {self.total} baht in change.')
        elif self.name == 'cappuccino' and self.total >= 80:
            self.water -= 250
            self.milk -= 50
            self.coffee -= 24
            self.total -= self.cost
            print(f'Here is {self.total} baht in change.')
        else:
            print("Sorry that's not enough money. Money refunded.")



class CoffeeMaker:
    def __init__(self):
        # every coffee machine has water, milk, and coffee = 1000
        self.water = 1000
        self.milk = 1000
        self.coffee = 1000


class MoneyMachine:
    def __init__(self):
        self.coffee_selected = input("What would you like? (latte/espresso/cappuccino): ")

        print("Please insert coins.")
        one_hundred = int(input("How many 100 baht coins?: "))
        fifty = int(input("How many 50 baht coins?: "))
        twenty = int(input("How many 20 baht coins?: "))
        ten = int(input("How many 10 baht coins?: "))
        five = int(input("How many 5 baht coins?: "))

        total = (one_hundred * 100) + (fifty * 50) + (twenty * 20) + (ten * 10) + (five * 5)
        print(f'Total amount inserted: {total} baht')

        Coffee(self.coffee_selected, total)


class ProductionReport:
    def get_ingredient_report(self, coffee_machine):
        print(f'Water: {coffee_machine.water} ml')
        print(f'Milk: {coffee_machine.milk} ml')
        print(f'Coffee: {coffee_machine.coffee} g')


coffee_maker = CoffeeMaker()
production_report = ProductionReport() 
production_report.get_ingredient_report(coffee_maker)  
money_machine = MoneyMachine() 
