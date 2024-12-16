class User:
    
    def __init__(self, income = 0, rent = 0, electricity = 0, internet_phone = 0, smartphone = 0, gym = 0, food_expenses = 0, saving = 0):
        self.income = income
        self.rent = rent
        self.electricity = electricity
        self.internet_phone = internet_phone
        self.smartphone = smartphone
        self.gym = gym
        self.food_expenses = food_expenses
        self.saving = saving

    def __repr__(self):
        pass



class Calculator:
    
    def __init__(self, fixed_cost = 50, pers_cost = 30, saving = 20):
        self.fixed_cost = fixed_cost
        self.pers_cost = pers_cost
        self.saving = saving

    def __repr__(self):
        pass


