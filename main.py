recipes = []

file = open("recipes.txt", "r")

for line in file:
    recipes.append(line.strip())

file.close()

print("recipes currently saved:")
print(recipes)

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
