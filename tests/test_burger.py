import pytest
import pytest_cov
from burger import Burger
from data import *


# Класс тестов для класса Burger
class TestBurger:
    # Тестируем создание пустого бургера
    def test_create_burger(self):
        my_burger = Burger()
        assert my_burger.bun == None and my_burger.ingredients==[]

    # Тестируем добавление булочки в бургер. bun_id - индекс булочки в моке
    @pytest.mark.parametrize('bun_id', [0, 1])
    def test_add_bun(self, bun_id, buns_and_ingredients):
        my_burger = Burger()
        bun = buns_and_ingredients[0][bun_id]
        my_burger.set_buns(bun)
        assert my_burger.bun == bun
    
    # Тестируем добавление булочки и замену на другую булочку в бургере
    def test_replace_bun(self, buns_and_ingredients):
        my_burger = Burger()
        my_burger.set_buns(buns_and_ingredients[0][0])
        my_burger.set_buns(buns_and_ingredients[0][1])
        assert my_burger.bun == buns_and_ingredients[0][1]
    
    # Тестируем добавление ингредиента в бургер. ingredient_id - индекс ингредиента в моке
    @pytest.mark.parametrize('ingredient_id', [0, 1])
    def test_add_ingredient(self, ingredient_id, buns_and_ingredients):
        my_burger = Burger()
        ingredient = buns_and_ingredients[1][ingredient_id]
        my_burger.add_ingredient(ingredient)
        assert my_burger.ingredients[0] == ingredient

    # Тестируем добавление ингредиентов и перемещение второго ингредиента на первое место
    def test_move_ingredient(self, buns_and_ingredients):
        my_burger = Burger()
        my_burger.add_ingredient(buns_and_ingredients[1][0])
        my_burger.add_ingredient(buns_and_ingredients[1][1])
        my_burger.move_ingredient(1,0)
        assert my_burger.ingredients[0] == buns_and_ingredients[1][1] and len(my_burger.ingredients) == 2

    # Тестируем добавление ингредиентов и удаление первого ингредиента
    def test_remove_ingredient(self, buns_and_ingredients):
        my_burger = Burger()
        my_burger.add_ingredient(buns_and_ingredients[1][0])
        my_burger.add_ingredient(buns_and_ingredients[1][1])
        my_burger.remove_ingredient(0)
        assert my_burger.ingredients[0] == buns_and_ingredients[1][1] and len(my_burger.ingredients) == 1

    # Тестируем расчет стоимости бургера. set_id - индекс набора булочка+ингредиент в моке
    @pytest.mark.parametrize('set_id', [0, 1])
    def test_get_price(self, set_id, buns_and_ingredients):
        my_burger = Burger()
        my_burger.set_buns(buns_and_ingredients[0][set_id])
        my_burger.add_ingredient(buns_and_ingredients[1][set_id])
        assert my_burger.get_price() == buns_and_ingredients[0][set_id].get_price() * 2 + buns_and_ingredients[1][set_id].get_price()

    # Тестируем вывод чека заказа на бургер. set_id - индекс набора булочка+ингредиент в моке
    @pytest.mark.parametrize('set_id', [0, 1])
    def test_get_receipt(self, set_id, buns_and_ingredients):
        my_burger = Burger()
        my_burger.set_buns(buns_and_ingredients[0][set_id])
        my_burger.add_ingredient(buns_and_ingredients[1][set_id])
        assert my_burger.get_receipt() == BunsIngredients.get_simple_receipt(buns_and_ingredients[0][set_id],buns_and_ingredients[1][set_id])
        
    
