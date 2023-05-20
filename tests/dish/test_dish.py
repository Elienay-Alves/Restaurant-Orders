from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish = Dish("Pizza", 28.9)

    with pytest.raises(ValueError):
        Dish("Pizza", 0)

    assert dish == Dish("Pizza", 28.9)
    assert dish.name == "Pizza"
    assert dish.price == 28.9
    assert hash(dish) == hash("Dish('Pizza', R$28.90)")
    assert repr(dish) == "Dish('Pizza', R$28.90)"

    dish.add_ingredient_dependency(Ingredient("Churrasco"), 1)

    assert dish.recipe == {Ingredient("Churrasco"): 1}
    assert {ingredient.name for ingredient in dish.get_ingredients()} == {
        "Churrasco"
    }
    assert not dish.get_restrictions()
