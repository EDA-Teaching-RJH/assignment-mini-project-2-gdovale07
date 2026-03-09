## project overview: this is a python coded recipe tracker, which allows for various recipes to be added, removed, edited, and searched for within the database, which the user can recall at any point as the recipes are saved in a text file, meaning they will be saved no matter what.

## object oriented programming: this code uses recipebooks to manage inputted recipes, it also has methods to add, delete, and search for recipes in a separate section which allows for better organisation within the code 

## file i/o: data stays in the system between runs of the code because it uses file handling to store data which has been inputted.

## regular expressions: the program has pythons re library which comes with the feature IGNORECASE, this allows for the user to search through recipes without the need to consider capital letters when typing, therefore improving the use experience.

## development process: i incrementally developed the code, slowly adding git commits to show improvements to my code. i started with a small setup and re library import, then added main menus, recipe recall, and organised my code into main and outside.

## challenges and problem solving: the main challenge i faced when writing this code was implementing the main() function. this caused severe indentation issues which took me a while to fix, however, after some research, i discovered that i could 1.) go back on myself to the point where i had just added the main() function, and 2.) simply highlight everything inside main() and press tab once so that the code was once again usable.

## future improvements: one thing which i think could be improved with this code, is adding the ability for methods and ingredients to be stored within the database, which would then need extra files so that each variation of a recipe (i.e pesto pasta, spaghetti bolognese) would remain stored under pasta, this would greatly enhance the user experience and allow for the code to become more useful and functional for real life use.