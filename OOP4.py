class Recipe:
    def __init__(self, name, ingredients, text, time):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.time = time

    def __str__(self):
        return self.name

    def __contains__(self, item):
        return item in self.ingredients

    def __gt__(self, other):
        return self.time > other.time

    def display_info(self):
        print(f"Рецепт: {self.name}")
        print(f"Час приготування: {self.time} хв")
        print(f"Інгредієнти: {', '.join(self.ingredients)}")
        print(f"Рецепт: {self.text}")


# Pizza = Recipe("Піца", ["борошно", "вода", "дріжджі", "томат", "сир"], "Готуємо тісто, додаємо інгредієнти та запікаємо", 30)
# Salad = Recipe("Салат", ["томат", "огірок", "зелень", "олія"], "Нарізаємо овочі, додаємо зелень та поливаємо олією", 10)
# Soup = Recipe("Суп", ["вода", "картопля", "морква", "м'ясо"], "Варимо всі інгредієнти до готовності", 45)
#
# print(Pizza.__str__())
# print(Salad.__contains__('томат'))
# print(Pizza.__gt__(Soup))
# Soup.display_info()
