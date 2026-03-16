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
def save_recipes(filename, recipes):
    file = open(filename, "w")
    for recipe in recipes:
        file.write(recipe + "\n")
    file.close()
##saves recipes to the recipe file
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
## removes recipes from the database
def main():## start of the running code
    book = recipebook("recipes.txt")

    while True:
        print("\n---recipe tracker menu---")
        print("1) view recipes")
        print("2) add recipe")
        print("3) search recipes")
        print("4) delete recipes")
        print("5) exit")
## main menu which contains options for user interaction
        choice = input("choose an option (1-5): ")
## asks user for an input from the main menu of options
        if choice == "1":
            print("\nrecipes currently saved:")
            if len(book.recipes) == 0:
                print("  (nothing saved yet)")
            else:
                for recipe in book.recipes:
                    print("-", recipe)
## displays all saved recipes for user to see        
        elif choice == "2":
            recipename = input("enter recipe name: ")

            if recipename.strip() == "":
                print("no input found, please enter again")
            else:
                book.add_recipe(recipename.strip())
                print("recipe saved.")
## saves inputted recipes into the database
        elif choice == "3":
            searchtext = input("search for a recipe: ")

            if searchtext.strip() == "":
                print("search cannot be empty, please try again")
            else:
                print("search results")
                found = False

                for recipe in book.recipes:
                    if re.search(searchtext, recipe, re.IGNORECASE):
                        print("-", recipe)
                        found = True
                
                if found == False:
                    print(" (no matches)")
## browses through recipe list to find user requested items        
        elif choice == "4":
            recipetodelete = input("emter the exact recipe name to delete")

            if recipetodelete.strip() == "":
                print("value cannot be empty, please try again")
            else:
                book.delete_recipe(recipetodelete.strip())
## deletes recipes from the database
        elif choice == "5":
            print("goodbye!")
            break

if __name__ == "__main__":
    main()