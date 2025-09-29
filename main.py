import json
import sys
from datetime import datetime
user = None
max_budget = 1000

with open("data/user.json", "r") as file:
    user = json.load(file)

print(user["budget"])

total_user_budget = user["budget"] + user["credit"]
if total_user_budget >= max_budget or total_user_budget < 0:
    print(f"There was a mistake. Your budget exceeds the maximum allowed budget of {max_budget}$ or is below 0$.")
    sys.exit() #or exit()
print(f"Hello! Your current budget is {total_user_budget}$ ")

expense = 0

expense_log = []
while expense <= 0 or expense > total_user_budget:
    expense = int(input("Please insert your expense amount or 'stop' to stop: \n"))

with open("logs/expense_log.txt", "a") as file:
    remaining_budget = total_user_budget - expense
    log_format = (f"\nAmount: {expense} "
                  f"UserID: {user["id"]} "
                  f"Budget: {total_user_budget} "
                  f"Remaining Budget: {remaining_budget} "
                  f"DateTime: {datetime.now()}")
    file.write(log_format)

#    expense_log += expense
#    expense = 0
#    if expense == 'stop'
#print(expense_log)

#expense_amount = expense
#id = user["id"]