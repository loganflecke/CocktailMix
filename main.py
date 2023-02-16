
import sys
import drinks

# import drinks

allIngredients = {
    'alcohol': [
            'whiskey', 'bourbon', 'scotch', 'irish whiskey', 'cinnamon whiskey',
        '', 'rum', 'spiced rum', 'white rum', 'gold rum', 'black rum', 'coconut rum', 'blueberry lemonade rum',
            'flavored rum',
        '', 'vodka', 'vanilla vodka',
        '', 'tequila', 'gold tequila',
        '', 'coffee liquer', 'amaretto liquer', 'orange liquer', 'moonshine', 'flavored moonshine', 'cognac',
        '', 'red wine', 'rose'],
    'mixers': [
        'orange juice', 'apple juice', 'lime juice', 'lemon juice', 'pineapple juice', 'grapefruit juice',
        '', 'cherries', 'orange', 'pineapple', 'lime', 'lemon',
        '', 'Coca-Cola', 'root beer', 'ginger-ale', 'ginger beer', 'Sprite', 'lemonade', 'club soda'],
    'others': [
        'ice', 'whipped cream', 'creamer', 'mint']
}

def main():
# list of all optional ingredients
# list of all the cocktails and their ingredients

    if len(sys.argv) < 2:
        help()
    elif sys.argv[1] == 'add':
        add(sys.argv[2])
    # elif sys.argv[1] == 'remove':
    #     removeIngredient(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'ingredients':
        listIngredients()
    elif sys.argv[1] == 'cocktails':
        listCocktails()
    elif sys.argv[1] == 'search':
        searchDrinks(sys.argv[2])
    elif (sys.argv[1] != None):
            if (sys.argv[1] in drinks.drinklist != None):
                printDrink(sys.argv[1])
            else:
                print("Enter a valid drink:")
                listCocktails()
    else:
        help()

def help():
    print('cocktails           View a list of all the cocktails available.')
    print('search ingredient   Search for all the cocktails containing '
          'your desired ingredient.')
    print('ingredients         View a list of all the ingredients.')
    print('add cocktail        Add a cocktail to the list. You will be prompted to '
          'add the ingredients.')
    print("[name of drink]     See the ingredients in [name of drink].")


# function to add a drink to the list
def add(name):
    print('List each ingredient for ' + name + ' one at a time.')
    print('If you are done, enter "done".')
    ingredients = [0 for i in range(10)]
    i = 0
    while (i < 11):
        print(i)
        print(ingredients[i])
        ingredients[i] = input('Next ingredient: ')
        if (ingredients[i] == "done"):
            ingredients[i] = 0
            break
        print(ingredients[i])
        i += 1
    tempDict = {name : ingredients}
    print(tempDict)
    addToList(tempDict)

# function to add element directly to drinklist
def addToList(tempDict):
    drinks.drinklist = (drinks.drinklist | tempDict)
    print(drinks.drinklist)

# function to view the entire list of cocktails
def listCocktails():
    for name in drinks.drinklist:
        print(name)

# function to view the entire list of ingredients
def listIngredients():
    for type in allIngredients:
        print(type)
        for ingredient in allIngredients[type]:
            print("     " + ingredient)

# function to search for all drinks with an ingredient
def searchDrinks(searchIngredient):
    for drink in drinks.drinklist:
        for ingredient in drinks.drinklist[drink]:
            if ingredient == searchIngredient:
                printDrink(drink)

# function to print the name of the drink followed by its ingredients
def printDrink(drink):
    print(drink)
    for ingredient in drinks.drinklist[drink]:
        print("     " + ingredient)


# function to remove an ingredient from a drink
# def removeIngredient(drink, ingredient):



if __name__ == '__main__':
    main()

