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

def main():
    book = recipebook("recipes.txt")

    while True:
        print("\n---recipe tracker menu---")
        print("1) view recipes")
        print("2) add recipe")
        print("3) search recipes")
        print("4) delete recipes")
        print("5) exit")

        choice = input("choose an option (1-5): ")

        if choice == "1":
            print("\nrecipes currently saved:")
            if len(book.recipes) == 0:
                print("  (nothing saved yet)")
            else:
                for recipe in book.recipes:
                    print("-", recipe)

        elif choice == "5":
            print("goodbye!")
            break
        else:
            print("option not added yet.")
            
        print("recipes currently saved:")

        if len(book.recipes) == 0:
            print("nothing saved yet")
        else:
            for recipe in book.recipes:
                print("-", recipe)

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

if __name__ == "__main__":
    main()