import pytest
from data import *

# фикстура забирает моки булочек и ингредиентов и возвращает их списками в списке
@pytest.fixture()
def buns_and_ingredients():
    buns = BunsIngredients.mock_buns
    ingredients = BunsIngredients.mock_ingredients
    return [buns, ingredients]