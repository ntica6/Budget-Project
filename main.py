import json
import sys

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

while expense <= 0 or expense > total_user_budget:
    expense = int(input("Please insert your expense amount: \n"))
