import json
import sys

# Define the name of the JSON file
drink_file = "drinks.json"
ingredients_file = "ingredients.json"

# Load the existing data from the JSON file
with open(drink_file, "r") as f:
    drinkList = json.load(f)
with open(ingredients_file, "r") as f:
    allIngredients = json.load(f)

def main():

    if len(sys.argv) < 2:
        print(open("banner.txt").read())
        help()
    elif sys.argv[1] == 'create':
        create(sys.argv[2], drinkList)
    elif sys.argv[1] == 'removeIngredient':
        removeIngredient(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'removeDrink':
       removeDrink(sys.argv[2],drinkList)
    elif sys.argv[1] == 'ingredients':
        listIngredients()
    elif sys.argv[1] == 'cocktails':
        listCocktails(drinkList)
    elif sys.argv[1] == 'search':
        searchDrinks(sys.argv[2], drinkList)
    elif (sys.argv[1] != None):
            if (sys.argv[1] in drinkList != None):
                printDrink(sys.argv[1], drinkList)
            else:
                print("Enter a valid drink:")
                listCocktails(drinkList)
    else:
        help()

def help():
    print('cocktails                View a list of all the cocktails available.')
    print('search ingredient        Search for all the cocktails containing '
          'your desired ingredient.')
    print('ingredients              View a list of all the ingredients.')
    print('create <cocktail>             Add a cocktail to the list. You will be prompted to '
          'add the ingredients.')
    print("removeDrink <name>       Remove a cocktail from the list.")
    print("<name of drink>          See the ingredients in [name of drink].")


# function to create a drink to the drinkList
def create(name, drinkList):
    print('List each ingredient for ' + name + ' one at a time.')
    print('If you are done, enter "done".')


    # examples array contains all the examples currently in concept
    if name in drinkList:
        ingredients = [drinkList[name]]
    else:
        ingredients = []

    while True:
        name = input('Next example: ')
        if (name != "done"):
                ingredients.append(name)
        else:
            break

    # add examples to tempDict
    tempDict = {name: ingredients}

    addToList(tempDict, drinkList)

# function to add element directly to drinks.json
def addToList(tempDict, drinkList):
    drinkList = drinkList | tempDict
    save_data(drinkList)

# function to view the entire list of cocktails
def listCocktails(drinkList):
    for name in drinkList:
        print(name)

# function to view the entire list of ingredients
def listIngredients():
    for type in allIngredients:
        print(type)
        for ingredient in allIngredients[type]:
            print("     " + ingredient)

# function to search for all drinks with an ingredient
def searchDrinks(searchIngredient, drinkList):
    for drink in drinkList:
        for ingredient in drinkList[drink]:
            if ingredient == searchIngredient:
                printDrink(drink, drinkList)

# function to print the name of the drink followed by its ingredients
def printDrink(drink, drinkList):
    print(drink)
    for ingredient in drinkList[drink]:
        print("     " + ingredient)


# function to remove an ingredient from a drink
def removeDrink(drink, drinkList):
    del drinkList[drink]
    save_data(drinkList)

# Define a function to remove an ingredient from a cocktail in the JSON data
def removeIngredient(name, ingredient):
    if name in drinkList:
        if ingredient in drinkList[name]:
            drinkList[name].remove(ingredient)
            save_data(drinkList)
        else:
            print(f"Ingredient '{ingredient}' not found in cocktail '{name}'.")
    else:
        print(f"Cocktail '{name}' not found.")

# Define a function to save the updated JSON data to the file
def save_data(drinkList):
    with open(drink_file, "w") as f:
        json.dump(drinkList, f, indent=4)


if __name__ == '__main__':
    main()

