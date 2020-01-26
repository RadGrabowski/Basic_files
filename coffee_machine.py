class CoffeeMachine:
    """
    A basic coffee machine simulator. Each instance contains the attributes describing the ingredients plus the money
    the machine has. It is possible to buy three types of coffee, fill the machine with ingredients, show their amount
    and finally take the money.
    """
    def __init__(self, water, milk, coffee, cups, money):
        self._water = water
        self._milk = milk
        self._coffee = coffee
        self._cups = cups
        self._money = money

    def run_option(self):
        """
        Runs the available options to manipulate the behaviour of the coffee machine.
        """
        func = input('Write action (buy, fill, take, remaining, exit): ')
        if func == 'buy':
            self._buy()
        elif func == 'fill':
            self._fill()
        elif func == 'take':
            self._take()
        elif func == 'remaining':
            self._remaining()
        elif func == 'exit':
            pass
        else:
            print('Function not found')
            self.run_option()

    def _buy(self):
        names = {self._water: 'water', self._milk: 'milk', self._coffee: 'coffee', self._cups: 'cups'}
        choice = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        if choice == '1':
            if self._water >= 250 and self._coffee >= 16 and self._cups >= 1:
                self._water -= 250
                self._coffee -= 16
                self._cups -= 1
                self._money += 4
                print('I have enough resources, making you a coffee!\n')
            else:
                print('Not enough ingredients!\n')
        elif choice == '2':
            if self._water >= 350 and self._milk >= 75 and self._coffee >= 20 and self._cups >= 1:
                self._water -= 350
                self._milk -= 75
                self._coffee -= 20
                self._cups -= 1
                self._money += 7
                print('I have enough resources, making you a coffee!\n')
            else:
                print('Sorry, not enough ingredients!\n')
        elif choice == '3':
            if self._water >= 200 and self._milk >= 100 and self._coffee >= 12 and self._cups >= 1:
                self._water -= 200
                self._milk -= 100
                self._coffee -= 12
                self._cups -= 1
                self._money += 6
                print('I have enough resources, making you a coffee!\n')
            else:
                print('Not enough ingredients!\n')
        elif choice == 'back':
            print()
        else:
            print('Wrong option, try again\n')
            self._buy()
        self.run_option()

    def _fill(self):
        self._water += int(input('\nWrite how many ml of water do you want to add: '))
        self._milk += int(input('Write how many ml of milk do you want to add: '))
        self._coffee += int(input('Write how many grams of coffee beans do you want to add: '))
        self._cups += int(input('Write how many disposable cups of coffee do you want to add: '))
        print()
        self.run_option()

    def _take(self):
        print('\nI gave you ${}\n'.format(self._money))
        self._money = 0
        self.run_option()

    def _remaining(self):
        print('''\nThe coffee machine has:
    {} of water
    {} of milk
    {} of coffee beans
    {} of disposable cups
    ${} of money\n'''.format(self._water, self._milk, self._coffee, self._cups, self._money))
        self.run_option()

print(help(CoffeeMachine))
machine = CoffeeMachine(400, 540, 120, 9, 550)
machine.run_option()
