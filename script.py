class User:
    
    def __init__(self, income = 0.0, rent = 0.0, electricity = 0.0, internet_phone = 0.0, smartphone = 0.0, gym = 0.0, food_expenses = 0.0, saving = 0.0):
        self.income = income
        self.fix_cost = rent + electricity + internet_phone
        self.saving = saving
        self.personal = gym + smartphone + food_expenses
        self.total_cost = self.fix_cost + self.saving + self.personal

    def __repr__(self):
        return "\nYou have an income of {user_income}€. Right now your monthly total cost are {total_cost}€. From that are the fixated cost {fix_cost}€, the cost for personel usage are {personel}€ and you are saving {saving}€.".format(user_income=self.income, total_cost=self.total_cost, fix_cost=self.fix_cost, personel=self.personal, saving=self.saving)

    def input(self, saving_personal, input):
        if saving_personal == "Saving":
            self.saving += input
            self.total_cost += input
        elif saving_personal == "Personal":
            self.personal += input
            self.total_cost += input
        elif saving_personal == "Fixed cost":
            self.fix_cost += input
            self.total_cost += input
        else:
            pass

class Calculator:
    
    def __init__(self, income):
        self.income = income
        self.perc1_income = 100 / income
        self.user_fix_perc = 0
        self.user_personal_perc = 0
        self.user_saving_perc = 0
        self.user_total = 0
        self.user_rest_perc = 0 
        self.fixed_cost_perc = 0.5
        self.pers_cost_perc = 0.3
        self.saving_perc = 0.2
        self.fixed_cost = income * self.fixed_cost_perc
        self.pers_cost = income * self.pers_cost_perc
        self.saving = income * self.saving_perc

    def __repr__(self):
        print("You have a income of {income}€. From the given input it is calculated you can use {fix_cost}€ for your fix cost, {pers_cost}€ for your personel cost and {saving}€ for your savings.".format(income=self.income, fix_cost=self.fixed_cost, pers_cost=self.pers_cost, saving=self.saving))

    #user input what he prefers (saving or personel cost). The user is able to enter how much percent of his income he will save/use for personel cost. 
    #The code will deduct which is not chosen.
    def prefer_saving(self, choice, input_percent):
        if choice == "Saving":
            self.saving_perc = input_percent / 100
            self.pers_cost_perc = 1.0 - (self.fixed_cost_perc + self.saving_perc)
            self.saving = self.income * self.saving_perc
            self.pers_cost = self.income * self.pers_cost_perc
            print("Your savings will be calculated with {saving_perc}% and your personel cost with {pers_cost_perc}%".format(saving_perc=self.saving_perc * 100, pers_cost_perc=self.pers_cost_perc * 100))
        else:
            self.pers_cost_perc = input_percent / 100
            self.saving_perc = 1.0 - (self.fixed_cost_perc + self.pers_cost_perc)
            self.pers_cost = self.income * self.pers_cost_perc
            self.saving = self.income * self.saving_perc
            print("Your personel cost will be calculated with {pers_cost_perc}% and your personel cost with {saving_perc}%".format(saving_perc=self.saving_perc * 100, pers_cost_perc=self.pers_cost_perc * 100))
        
    #if the fix cost is under 50%, it will add the remaining percent (of 50) to either savings or personal cost
    def fix_under_50(self, choice, user_fixcost):
        rest_perc = self.fixed_cost_perc - (user_fixcost * self.perc1_income) / 100
        self.fixed_cost_perc = self.fixed_cost_perc - rest_perc
        if choice == "Personel":
            self.pers_cost_perc += rest_perc
        else:
            self.saving_perc += rest_perc

    #if the fix cost is over 50%, it will deduct the percent over 50% from either savings or personel cost
    def fix_over_50(self, choice, user_fixcost):
        over_perc = (user_fixcost * self.perc1_income) - 0.5
        self.fixed_cost_perc = self.fixed_cost_perc + over_perc
        if choice == "Saving":
            self.saving_perc -= over_perc
        else:
            self.pers_cost_perc -= over_perc

    #calculates the given costs in percent and tells the user if he has a rest or is living over his wage
    def income_in_perc(self, user_fix, user_personal, user_saving):
        self.user_fix_perc = user_fix * self.perc1_income
        self.user_personal_perc = user_personal * self.perc1_income
        self.user_saving_perc = user_saving * self.perc1_income
        self.user_total = self.user_fix_perc + self.user_personal_perc + self.user_saving_perc
        self.user_rest_perc = 100 - self.user_total
        if self.user_rest_perc > 0:
            print("Currently your income is splitted in {fix}% fixed cost, {pers}% personal cost and {save}% savings. You are not using {rest}% of your income.".format(fix=round(self.user_fix_perc, 2), pers=round(self.user_personal_perc, 2), save=round(self.user_saving_perc, 2), rest=round(self.user_rest_perc, 2)))
            user_input = input("Now please choose how you want to use your rest percentage. You can either split it 50/50 to your savings and personal cost, put it all in your savings or use it all for your personal cost. \nOf course u can let it be as it is too (not recommended)! Please choose: Split|Saving|Personal|Nothing ")
            if user_input == "Split":
                self.user_personal_perc += self.user_rest_perc / 2
                self.user_saving_perc += self.user_rest_perc / 2
                print("Added {rest}% to your personal costs and savings".format(rest=round(self.user_rest_perc / 2, 2)))
                print("Your income is now splitted in {fix}% fix costs, {pers}% personal costs and {save}% savings.".format(fix=round(self.user_fix_perc, 2), pers=round(self.user_personal_perc, 2), save=round(self.user_saving_perc, 2)))
                print("Which are as a number: {fix}€ fix costs, {pers}€ personal costs and {save}€ savings.".format(fix=round((self.user_fix_perc / 100) * self.income, 2), pers=round((self.user_personal_perc / 100) * self.income, 2), save=round((self.user_saving_perc / 100) * self.income, 2)))
            elif user_input == "Saving":
                self.user_saving_perc += self.user_rest_perc
                print("Added {rest}% to your savings".format(rest=round(self.user_rest_perc, 2)))
                print("Your income is now splitted in {fix}% fix costs, {pers}% personal costs and {save}% savings.".format(fix=round(self.user_fix_perc, 2), pers=round(self.user_personal_perc, 2), save=round(self.user_saving_perc, 2)))
                print("Which are as a number: {fix}€ fix costs, {pers}€ personal costs and {save}€ savings.".format(fix=round((self.user_fix_perc / 100) * self.income, 2), pers=round((self.user_personal_perc / 100) * self.income, 2), save=round((self.user_saving_perc / 100) * self.income, 2)))
            elif user_input == "Personal":
                self.user_personal_perc += self.user_rest_perc
                print("Added {rest}% to your personal costs".format(rest=round(self.user_rest_perc, 2)))
                print("Your income is now splitted in {fix}% fix costs, {pers}% personal costs and {save}% savings.".format(fix=round(self.user_fix_perc, 2), pers=round(self.user_personal_perc, 2), save=round(self.user_saving_perc, 2)))
                print("Which are as a number: {fix}€ fix costs, {pers}€ personal costs and {save}€ savings.".format(fix=round((self.user_fix_perc / 100) * self.income, 2), pers=round((self.user_personal_perc / 100) * self.income, 2), save=round((self.user_saving_perc / 100) * self.income, 2)))
            else:
                print("You decided to do nothing with your rest percentage.")
                print("Your income remains splitted in {fix}% fixed cost, {pers}% personal cost and {save}% savings. You are not using {rest}% of your income.".format(fix=round(self.user_fix_perc, 2), pers=round(self.user_personal_perc, 2), save=round(self.user_saving_perc, 2), rest=round(self.user_rest_perc, 2)))
                print("Which are as a number: {fix}€ fix costs, {pers}€ personal costs and {save}€ savings. You are not using {rest}€ of your income.".format(fix=round((self.user_fix_perc / 100) * self.income, 2), pers=round((self.user_personal_perc / 100) * self.income, 2), save=round((self.user_saving_perc / 100) * self.income, 2), rest=round((self.user_rest_perc / 100) * self.income, 2)))
        else:
            over = self.user_total - 100
            print("You are living {over_perc}% over your wage. Please seek a financial advisor.".format(over_perc=round(over, 2)))






#Welcoming message!
print("This program is a living expenses calculator. \nIt will ask you some personal questions to calculate with your monthly wage your living expenses in three sections: \n1. Fixed costs \n2. Personal Costs (like gym membership or pocketmoney) \n3. Money you are saving \nIt will also give you the option to prefer saving your money or using your money for personal costs. \nLet\'s get started: \n \n \n \n")

user_income = float(input("How much are you earning monthly? "))
user_rent = float(input("How much are you paying for rent? "))
user_electricity = float(input("How high is your electricity bill? "))
user_internet = float(input("How much are you paying for your internet connection? "))
user_smartphone = float(input("What is your monthly bill for your smartphone and LTE usage? "))
user_gym = float(input("If you have a gym membership: how high are the cost? (Just right 0 if you have no membership) "))
user_food = float(input("How much are you paying approxiamtly monthly for your food? "))
user_saving = float(input("For your income how much are you saving montly right now? (If nothing just write 0) "))

user1 = User(user_income, user_rent, user_electricity, user_internet, user_smartphone, user_gym, user_food, user_saving)
calc = Calculator(user_income)

#Logic for a user input
def user_input():
    add_quest = input("\nDo you have aynthing to add? Yes|No ")
    if add_quest == "Yes":
        how_much = float(input("How much do you want to add? "))
        where = input("Where do you want to add it to? Fixed cost|Saving|Personal ")
        user1.input(where, how_much)
        print("\nYou added {cost} to your {add}.".format(cost=how_much, add=where))
        user_input()
    else:
        print("\nYou have nothing to add.")

user_input()

print(user1)

calc.income_in_perc(user1.fix_cost, user1.personal, user1.saving)
    

#Logic if User prefers saving, personel or wants the default

#choice_prefer = input("Saving, Personal or Default? ")
#if choice_prefer == "Saving" or choice_prefer == "Personel":
#    percent = float(input("How much? (Cannot be higher than 50%) "))
#    calc.prefer_saving(choice_prefer, percent)
#else:
#     pass








