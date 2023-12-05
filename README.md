# CocktailMix 🍹

CocktailMix is a command-line Python tool that serves as your personalized cocktail drink recipe book. With CocktailMix, you can easily create and enjoy a wide variety of drinks by combining different ingredients. The tool stores ingredients and drinks in a JSON file, allowing you to customize your cocktail library to suit your taste.

## Features

- **Create Custom Drinks**: Mix and match ingredients to create your own unique cocktails.
- **Ingredient Library**: Easily add, remove, and update ingredients in your library.
- **Save and Share Recipes**: Save your favorite drink recipes and share them with friends.
- **Simple and Intuitive**: Command-line interface for a straightforward and user-friendly experience.

## Installation

Make sure you have Python 3 installed on your system. Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/CocktailMix.git
cd CocktailMix
pip install -r requirements.txt
```

## Usage

### 1. View Available Ingredients

```bash
python cocktailmix.py ingredients
```

This command displays a list of available ingredients with their IDs.

### 2. Create a New Drink

```bash
python cocktailmix.py create
```

Follow the prompts to choose ingredients and provide a name for your custom drink.

### 3. View Saved Drinks

```bash
python cocktailmix.py drinks
```

List all the saved drinks with their names and ingredients.

### 4. Share a Recipe

```bash
python cocktailmix.py share <drink_name>
```

Replace `<drink_name>` with the name of the drink you want to share. This command generates a shareable link with the recipe.

### 5. Add New Ingredient

```bash
python cocktailmix.py add-ingredient
```

Follow the prompts to add a new ingredient to your library.

## Configuration

Configure your drink library by editing the `drinks.json` file. Customize the ingredients, drinks, and their respective recipes.

## Contributing

Found a bug or want to contribute? Feel free to open an issue or submit a pull request. Your contributions are highly welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Cheers to your mixology adventures with CocktailMix! 🥂
