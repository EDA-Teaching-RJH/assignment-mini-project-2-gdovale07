recipes = []

file = open("recipes.txt", "r")

for line in file:
    recipes.append(line.strip())

file.close()
            
recipename = input("enter name of recipe")
recipes.append(recipename)

print("recipe tracker has now started")
print("recipes:", recipes)

file = open("recipes.txt", "w")

for recipe in recipes:
    file.write(recipe + "/n")

file.close()
