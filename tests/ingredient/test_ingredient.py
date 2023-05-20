from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("leite")

    assert repr(ingredient) == "Ingredient('leite')"
    assert hash(ingredient) == hash("leite")
    assert ingredient.name == "leite"
    assert ingredient == Ingredient("leite")
    assert not ingredient.restrictions
