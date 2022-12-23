# Utility maximizing formula: (utility of item) / (cost of item)

# Function to calculate the utility maximizing formula
def calc_util_maximizing_formula(utility, cost):
  return utility / cost

# Function to determine the best decision for purchasing items
def determine_best_decision(items):
  best_item = None
  max_util_per_cost = 0

  for item in items:
    util_per_cost = calc_util_maximizing_formula(item['utility'], item['cost'])
    if util_per_cost > max_util_per_cost:
      max_util_per_cost = util_per_cost
      best_item = item

  return best_item

# (name) Want - (Item)enjoyment/need - (cost)cost/time
items = [

  {'name': 'Item1', 'utility': 10, 'cost': 80},
  {'name': 'Item2', 'utility': 9, 'cost': 70},
  {'name': 'Item3', 'utility': 6, 'cost': 40},
]

best_item = determine_best_decision(items)
print(f'The best item to purchase is {best_item["name"]} with a utility of {best_item["utility"]} and a cost of {best_item["cost"]}')