"""
Creates a dictionary of dictionaries from three lists: menu, meals, days; and
provides the answer to a query about the special of the day.
There are two versions of the code that creates the dictionary of dictionaries, 
labelled "Succinct verion" and "Wordy version" below. Both do essentially the
same thing, but the "Succinct version" does it in a single statement.
"""

import sys

day, meal = sys.argv[1].capitalize(), sys.argv[2].lower()

menu = [
    ("scones", "quesadillas", "veg lasagna"),
    ("oatmeal", "veg burgers", "veg chili"),
    ("pancakes", "salad", "veg curry"),
    ("croissants", "burritos", "pad thai"),
    ("waffles", "calzones", "pizza"),
    ("brownies", "veg kabobs", "broccoli quiche"),
    ("eggs", "tortas", "penne with pesto")
    ]

meals = ["breakfast", "lunch", "dinner"]

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Succinct version
specials = dict(zip(days, [dict(zip(meals, items)) for items in menu]))
print("\nDictionary from succinct version:\n", specials)

#Wordy version
specials_list = []
for items in menu:
    zipped_meals_items_dict = dict(zip(meals, items))
    specials_list.append(zipped_meals_items_dict)
specials1 = dict(zip(days, specials_list))
print("\nDictionary from wordy version:\n", specials1)

if day not in days:
    print("\n'"+day+"'", "is not valid. Please enter a valid day of the week.")
if meal not in meals:
    print("\n'"+meal+"'", "is not valid. Please enter a valid meal ('breakfast', 'lunch' or 'dinner').")
if day in days and meal in meals:
    print("\nThe special for", day, meal, "will be", specials[day][meal]+".")
