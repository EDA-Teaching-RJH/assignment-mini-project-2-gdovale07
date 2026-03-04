def start_program():
    print("program started")

class RecipeBook:
    def __init__(self):
        self.recipes = []

start_program()
book = RecipeBook()
print("recipe tracker started")
print("number of recipes:", len(book.recipes))

start_program()