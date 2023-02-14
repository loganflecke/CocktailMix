import json

def addDrink(name, ingredient):
    json.dump(name, ingredient)


drinks = {
    'mojito' : ['white rum', 'mint', 'club soda'],
    'margherita' : ['tequila', 'triple sec', 'lime juice'],
    'tequila shot' : ['tequila', 'salt', 'lime']
    }