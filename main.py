import re

def load_recipes(filename):
    recipes = []

    file = open(filename, "r")
    for line in file:
        recipe = line.strip()
        if recipe != "":
            recipes.append(recipe)
    file.close()

    return recipes

recipes = load_recipes("recipes.txt")

print("recipes currently saved:")

if len(recipes) == 0:
    print("nothing saved yet")
else:
    for recipe in recipes:
        print("-", recipe)
        
searchtext = input("search for a recipe or press enter to skip")

if searchtext != "":
    print("search results")

    for recipe in recipes:
        if re.search(searchtext, recipe, re.IGNORECASE):
            print(recipe)

while True:
    recipename = input("enter recipe name or type 'done' to finish: ")

    if recipename.lower() == "done":
        break

    if recipename.strip == "":
        print("no input found, please enter again")
    else:
        recipes.append(recipename.strip())


print("recipe tracker has now started")
print("recipes:", recipes)

file = open("recipes.txt", "w")

for recipe in recipes:
    file.write(recipe + "/n")

file.close()
