def cakes(recipe, ingredients):
    possible_cake = 0
    counter = 0
    if len(recipe) > len(ingredients):
        return possible_cake
    else:
        for ing_material, ing_amounts in ingredients.items():
            for rec_material, rec_amounts in recipe.items():
                if ing_material == rec_material:
                    counter += 1
                    cake_ratio = ing_amounts // rec_amounts
                if counter == len(recipe):
                    if possible_cake == 0 and cake_ratio != 0:
                        possible_cake = cake_ratio
                    elif cake_ratio < possible_cake:
                        possible_cake = cake_ratio
                else:
                    possible_cake = 0
        return possible_cake


def main():
    recipes_list = [
        {
            "name": "Pound Cake",
            "ingredients": {"flour": 500, "sugar": 200, "eggs": 1}
        },
        {
            "name": "Vanilla Cake",
            "ingredients": {"flour": 500, "sugar": 200, "eggs": 1, "vanilla": 2}
        },
        {
            "name": "Apple Cake",
            "ingredients": {"flour": 500, "sugar": 200, "eggs": 1, "apples": 5}
        }
    ]
    available_ingredients = {"flour": 1200, "sugar": 1200, "eggs": 5, "vanilla": 200}
    # for i in range(len(recipes_list)):
    print("Your ingredients enables you to bake the following cakes: ")
    for recipe in recipes_list:
        possible_cake = cakes(recipe["ingredients"], available_ingredients)
        # print(possible_cake)
        if possible_cake != 0:
            print(str(recipe["name"]))


main()
