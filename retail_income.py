class RentalPropertyCalculator:
    def __init__(self, purchase_price = 0, monthly_rent = 0, annual_expenses = 0, holding_period = 0):
        self.purchase_price = purchase_price
        self.monthly_rent = monthly_rent
        self.annual_expenses = annual_expenses
        self.holding_period = holding_period

    # def user_questions(self):
    #     self.purchase_price = float(input("Enter the purchase price for your property: "))
    #     self.monthly_rent = float(input("Enter the property's monthly rent: "))
    #     self.annual_expenses = float(input("Enter the annual expenses: "))
    #     self.holding_period = int(input("In years, enter the holding period: "))
    
    def calculate_roi(self):
        total_rental_income = self.monthly_rent * 12 * self.holding_period
        total_expenses = self.annual_expenses * self.holding_period
        total_profit = total_rental_income - self.purchase_price - total_expenses
        roi = (total_profit / (self.purchase_price + total_expenses)) * 100
        return roi
    
    def user_questions(self):
        self.purchase_price = float(input("Enter the purchase price for your property: "))
        self.monthly_rent = float(input("Enter the property's monthly rent: "))
        self.annual_expenses = float(input("Enter the annual expenses: "))
        self.holding_period = int(input("In years, enter the holding period: "))

        calculator = RentalPropertyCalculator(self.purchase_price, self.monthly_rent, self.annual_expenses, self.holding_period)
        roi = calculator.calculate_roi()

        print(f"\nReturn on Investment (ROI) over {self.holding_period} years: {roi:.2f}%")

    def runner(self):
        while True:
            check_point = input("Enter 'run' to start the program or 'quit' to end the program: ").lower()
            if check_point == "run":
                self.user_questions()
            elif check_point == "quit":
                break
            else:
                print("Bad input, try again.")


my_roi = RentalPropertyCalculator()

my_roi.runner()



    

