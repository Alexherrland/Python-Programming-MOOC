# Write your solution here
def obtain_recipes(recipes_file):
    with open(f"src/{recipes_file}") as recipes1:
    #with open(recipes_file) as recipes1:
        document = [line.strip() for line in recipes1]
    recipes = {}
    cont = 1
    for line in document:
        if line == "":
            cont += 1
            continue
        if line not in recipes and cont == 1:
            recipes[line] = []
            index = line
            cont = 0
        else:
            recipes[index].append(line)
    return recipes


def search_by_name(filename: str, word: str):
    recipes = obtain_recipes(filename)
    list_recipes = []
    for name_recipe, values in recipes.items():
        if word.lower() in name_recipe.lower():
            list_recipes.append(name_recipe)
    return list_recipes

def search_by_time(filename: str, prep_time: int):
    recipes = obtain_recipes(filename)
    list_recipes = []
    for name_recipe, values in recipes.items():
        if int(values[0]) <= prep_time:
            list_recipes.append(f"{name_recipe}, preparation time {values[0]} min")
    return list_recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipes = obtain_recipes(filename)
    list_recipes = []
    for name_recipe, values in recipes.items():
        possible_ingredients = values[1:len(values)]
        if ingredient.lower() in possible_ingredients:
            list_recipes.append(f"{name_recipe}, preparation time {values[0]} min")
    return list_recipes

if __name__ == "__main__":

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)
        