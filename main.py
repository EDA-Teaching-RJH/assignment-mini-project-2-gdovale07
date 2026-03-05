class RecipeBook:
    def __init__(self, filename):
        self.filename = filename
        self.recipes = []
        self.load()