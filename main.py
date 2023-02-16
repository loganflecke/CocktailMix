import json
import sys

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
    drinkList = json.load(open("drinks.json"))


    if len(sys.argv) < 2:
        help()
    elif sys.argv[1] == 'add':
        add(sys.argv[2], drinkList)
    # elif sys.argv[1] == 'remove':
    #     removeIngredient(sys.argv[2], sys.argv[3])
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
    print('cocktails           View a list of all the cocktails available.')
    print('search ingredient   Search for all the cocktails containing '
          'your desired ingredient.')
    print('ingredients         View a list of all the ingredients.')
    print('add cocktail        Add a cocktail to the list. You will be prompted to '
          'add the ingredients.')
    print("[name of drink]     See the ingredients in [name of drink].")


# function to add a drink to the list
def add(name, drinkList):
    print('List each ingredient for ' + name + ' one at a time.')
    print('If you are done, enter "done".')
    tempDict = {name : ""}

    ingredients = []
    i = 0
    while (i < 10):
        ingredient = input('Next ingredient: ')
        if (ingredient != "done"):
            ingredients.append(ingredient)
        else:
            break
        i += 1

    tempDict[name] = ingredients
    addToList(tempDict, drinkList)

# function to add element directly to drinklist
def addToList(tempDict, drinkList):
    drinkList = drinkList | tempDict
    with open("drinks.json", "w") as jsonFile:
        json.dump(drinkList, jsonFile, indent=4)

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
# def removeIngredient(drink, ingredient):


if __name__ == '__main__':
    main()

