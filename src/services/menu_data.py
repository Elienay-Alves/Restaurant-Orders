# Req 3
from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = set()
        self.load_menu()

    def read_file(self, path: str) -> list[str]:
        with open(path, mode="r", encoding="utf-8") as file:
            file = csv.reader(file)
            return list(file)

    def load_menu(self):
        lines = self.read_file(self.path)

        for line in lines[1:]:
            name = line[0]
            price = float(line[1])
            ingredient_name = line[2]
            amount = int(line[3])
            dish = next(
                (item for item in self.dishes if item == Dish(name, price)),
                None,
            )
            if dish is None:
                dish = Dish(name, float(price))
                self.dishes.add(dish)

            ingredient = Ingredient(ingredient_name)
            dish.add_ingredient_dependency(ingredient, int(amount))
