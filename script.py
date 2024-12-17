class User:
    
    def __init__(self, income = 0.0, rent = 0.0, electricity = 0.0, internet_phone = 0.0, smartphone = 0.0, gym = 0.0, food_expenses = 0.0, saving = 0.0):
        self.income = income
        self.fix_cost = rent + electricity + internet_phone
        self.saving = saving
        self.personal = gym + smartphone + food_expenses
        self.total_cost = self.fix_cost + self.saving + self.personal

    def __repr__(self):
        pass

    def input1(self, choice, saving_personal, input):
        if choice == "Yes" and saving_personal == "Saving":
            self.saving += input
        elif choice == "Yes" and saving_personal == "Personal":
            self.personal += input
        else:
            pass

class Calculator:
    
    def __init__(self, income):
        self.income = income
        self.perc1_income = 100 / income 
        self.fixed_cost_perc = 0.5
        self.pers_cost_perc = 0.3
        self.saving_perc = 0.2
        self.fixed_cost = income * self.fixed_cost_perc
        self.pers_cost = income * self.pers_cost_perc
        self.saving = income * self.saving_perc

    def __repr__(self):
        pass

    #user input what he prefers (saving or personel cost). The user is able to enter how much percent of his income he will save/use for personel cost. 
    #The code will deduct which is not chosen.
    def prefer_saving(self, choice, input_percent):
        if choice == "Saving":
            self.saving_perc = input_percent / 100
            self.pers_cost_perc = 1.0 - (self.fixed_cost_perc + self.saving_perc)
            self.saving = self.income * self.saving_perc
            self.pers_cost = self.income * self.pers_cost_perc
        else:
            self.pers_cost_perc = input_percent / 100
            self.saving_perc = 1.0 - (self.fixed_cost_perc + self.pers_cost_perc)
            self.pers_cost = self.income * self.pers_cost_perc
            self.saving = self.income * self.saving_perc
        
    #if the fix cost is under 50%, it will add the remaining percent (of 50) to either savings or personal cost
    def under_50(self, choice, user_fixcost):
        if user_fixcost < self.fixed_cost:
            rest_perc = self.fixed_cost_perc - (user_fixcost * self.perc1_income) / 100
            self.fixed_cost_perc = self.fixed_cost_perc - rest_perc
            if choice == "Personel":
                self.pers_cost_perc += rest_perc
            else:
                self.saving_perc += rest_perc





#Welcoming message!
print("This program is a living expenses calculator. \nIt will ask you some personal questions to calculate with your monthly wage your living expenses in three sections: \n1. Fixed costs \n2. Personal Costs (like gym membership or pocketmoney) \n3. Money you are saving \nIt will also give you the option to prefer saving your money or using your money for personal costs. \nLet\'s get started: \n \n \n \n")

user_income = float(input("How much are you earning monthly? "))


user1 = User(rent=100, electricity=50, internet_phone=50)
calc = Calculator(user_income)



#Logic if User prefers saving, personel or wants the default

#choice_prefer = input("Saving, Personal or Default? ")
#if choice_prefer == "Saving" or choice_prefer == "Personel":
#    percent = float(input("How much? (Cannot be higher than 50%) "))
#    calc.prefer_saving(choice_prefer, percent)
#else:
#     pass


#Logic for a user input

#choice = input("Do you want to add something | Yes/No")
#if choice == "Yes":
#    cash = float(input("Please enter how much:"))
#    choice2 = input("Do you want to add it do your savings or personal costs | Enter: Saving/Personal")
#user1.input1(choice, choice2, cash)





