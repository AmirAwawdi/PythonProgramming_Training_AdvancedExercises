def cakes(recipe, ingredients):
    max_cakes = 0
    if len(recipe) > len(ingredients):
        return max_cakes
    else:
        for ing_material, ing_amounts in ingredients.items():
            for rec_material, rec_amounts in recipe.items():
                if ing_material == rec_material:
                    cake_ratio = ing_amounts // rec_amounts
                if max_cakes == 0 and cake_ratio != 0:
                    max_cakes = cake_ratio
                elif cake_ratio < max_cakes:
                    max_cakes = cake_ratio
        return max_cakes


def main():
    print("Enter cake's recipe: ")
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    print(recipe)
    print("Enter the available ingredients: ")
    ingredients = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(ingredients)
    # recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    # ingredients = {"sugar": 500, "flour": 2000, "milk": 2000}
    max_cakes = cakes(recipe, ingredients)
    print("Your ingredients enables you to provide maximum of " + str(max_cakes) + " cakes according to the given recipe")


main()
