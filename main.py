
import json
import sys

import drinks

allIngredientsJSON = {
    'alcohol': ['whiskey', 'bourbon', 'scotch', 'irish whiskey', 'cinnamon whiskey', '', 'rum', 'spiced rum', 'white rum',
                'gold rum', 'black rum', 'coconut rum', 'blueberry lemonade rum', 'flavored rum', '', 'vodka',
                'vanilla vodka', '', 'tequila', 'gold tequila', '', 'coffee liquer', 'amaretto liquer', 'orange liquer',
                'moonshine', 'flavored moonshine', 'cognac', '', 'red wine', 'rose'],
    'mixers': [
        'orange juice', 'apple juice', 'lime juice', 'lemon juice', 'pinapple juice',
                    'grapefruit juice', '', 'cherries', 'orange', 'pineapple', '', 'Coca-Cola',
                    'root beer', 'ginger-ale', 'ginger beer', 'Sprite'],
    'others': ['ice', 'whipped cream', 'creamer', ]
}

def main():
# list of all optional ingredients
# list of all the cocktails and their ingredients

    if sys.argv[1] == 'add':
        add(sys.argv[2])
    # elif sys.argv[1] == 'remove':
    #     removeIngredient(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'ingredients':
        listIngredients()
    # elif sys.argv[1] == 'cocktails':
    #     listCocktails()
    # elif sys.argv[1] == 'search':
    #     searchDrinks(sys.argv[2])
    else:
        print('Type "cocktails" to view a list of all the cocktails available.')
        print(
            'Type "search" followed by an ingredient to search for all the cocktails containing your desired ingredient.')
        print('Type "ingredients" to view a list of all the ingredients included.')
        print(
            'Type "add" followed by the name to add a cocktail to the list. You will be prompted to add the ingredients.')
        print()
        print('Try again.')

# function to add a drink to the list
def add(name):
    allIngredients = json.loads(allIngredientsJSON)
    # add name to drink in json
    drinks.addDrink(name)

    print('List each ingredient for ' + name + ' one at a time.')
    print('If you are done, enter "done".')
    ingredient = ''

    while (ingredient != 'done'):
        ingredient = input('Next ingredient: ')
        # validate that ingredient is in list
        if (allIngredients.get(ingredient) is None):
            print('Enter a valid ingredient or cancel and enter "ingredients" to view them all.')
            break
        # add ingredient to drink in json
        drinks.addDrink(ingredient, name)

# function to view the entire list of cocktails
# def listCocktails():

# function to view the entire list of ingredients
def listIngredients():
    for type in allIngredientsJSON:
        print(type)
        for ingredient in allIngredientsJSON[type]:
            print("     " + ingredient)

# function to search for all drinks with an ingredient
# def searchDrinks(ingredient):


# function to remove an ingredient from a drink
# def removeIngredient(drink, ingredient):



if __name__ == '__main__':
    main()

