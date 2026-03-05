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

class recipebook:
    def __init__(self, filename):
        self.filename = filename
        self.recipes = load_recipes(filename)

    def save(self):
        save_recipes(self.filename, self.recipes)

    def add_recipe(self, recipe_name):
        self.recipes.append(recipe_name)
        self.save()
    
    def delete_recipe(self, recipe_name):
        if recipe_name in self.recipes:
            self.recipes.remove(recipe_name)
            self.save()
            print("recipe deleted")
        else:
            print("recipe not found")

book = recipebook("recipes.txt")

print("recipes currently saved:")

if len(book.recipes) == 0:
    print("nothing saved yet")
else:
    for recipe in book.recipes:
        print("-", recipe)

def save_recipes(filename, recipes):
    file = open(filename, "w")

    for recipe in recipes:
        file.write(recipe + "\n")

    file.close()

searchtext = input("search for a recipe or press enter to skip")

if searchtext != "":
    print("search results")

    for recipe in book.recipes:
        if re.search(searchtext, recipe, re.IGNORECASE):
            print(recipe)

deletechoice = input("do you want to delete a recipe? y/n: ")

if deletechoice.lower() == "y":
    recipetodelete = input("enter exact recipe name to delete")
    book.delete_recipe(recipetodelete)

while True:
    recipename = input("enter recipe name or type 'done' to finish: ")

    if recipename.lower() == "done":
        break

    if recipename.strip() == "":
        print("no input found, please enter again")
    else:
        book.add_recipe(recipename.strip())


print("recipe tracker has now started")
print("recipes:", book.recipes)