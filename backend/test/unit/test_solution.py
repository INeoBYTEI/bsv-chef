import pytest
from unittest.mock import MagicMock, patch
from src.controllers.recipecontroller import RecipeController
from src.util.dao import DAO
from src.static.diets import Diet

@pytest.fixture
def mock_dao():
    dao_mock = MagicMock(spec=DAO)
    return dao_mock

@pytest.fixture
def controller(mock_dao):
    return RecipeController(items_dao=mock_dao)

@patch('src.util.calculator.calculate_readiness')
def test_get_recipe_normal_optimal(mock_calculate_readiness, controller, mock_dao):
    mock_dao.get_all.return_value = [
        {"name": "item1", "quantity": 5},
        {"name": "item2", "quantity": 3}
    ]
    controller.recipes = [
        {"name": "recipe1", "diets": ["normal"], "ingredients": {"item1": 1, "item2": 2}},
        {"name": "recipe2", "diets": ["normal"], "ingredients": {"item1": 5, "item2": 3}}
    ]
    mock_calculate_readiness.side_effect = [0.5, 1.0]

    result = controller.get_recipe(Diet.NORMAL, take_best=True)

    assert result["name"] == "recipe2"
    mock_dao.get_all.assert_called_once()

@patch('src.util.calculator.calculate_readiness')
def test_get_recipe_normal_random(mock_calculate_readiness, controller, mock_dao):
    mock_dao.get_all.return_value = [
        {"name": "item1", "quantity": 5},
        {"name": "item2", "quantity": 3}
    ]
    controller.recipes = [
        {"name": "recipe1", "diets": ["normal"], "ingredients": {"item1": 1, "item2": 2}},
        {"name": "recipe2", "diets": ["normal"], "ingredients": {"item1": 5, "item2": 3}}
    ]
    mock_calculate_readiness.side_effect = [0.5, 1.0]

    result = controller.get_recipe(Diet.NORMAL, take_best=False)

    assert result["name"] in ["recipe1", "recipe2"]
    mock_dao.get_all.assert_called_once()

@patch('src.util.calculator.calculate_readiness')
def test_get_recipe_vegetarian_optimal(mock_calculate_readiness, controller, mock_dao):
    mock_dao.get_all.return_value = [
        {"name": "item1", "quantity": 5},
        {"name": "item2", "quantity": 3}
    ]
    controller.recipes = [
        {"name": "recipe1", "diets": ["vegetarian"], "ingredients": {"item1": 1, "item2": 2}},
        {"name": "recipe2", "diets": ["vegetarian"], "ingredients": {"item1": 5, "item2": 3}}
    ]
    mock_calculate_readiness.side_effect = [0.5, 1.0]

    result = controller.get_recipe(Diet.VEGETARIAN, take_best=True)

    assert result["name"] == "recipe2"
    mock_dao.get_all.assert_called_once()

@patch('src.util.calculator.calculate_readiness')
def test_get_recipe_vegetarian_random(mock_calculate_readiness, controller, mock_dao):
    mock_dao.get_all.return_value = [
        {"name": "item1", "quantity": 5},
        {"name": "item2", "quantity": 3}
    ]
    controller.recipes = [
        {"name": "recipe1", "diets": ["vegetarian"], "ingredients": {"item1": 1, "item2": 2}},
        {"name": "recipe2", "diets": ["vegetarian"], "ingredients": {"item1": 5, "item2": 3}}
    ]
    mock_calculate_readiness.side_effect = [0.5, 1.0]

    result = controller.get_recipe(Diet.VEGETARIAN, take_best=False)

    assert result["name"] in ["recipe1", "recipe2"]
    mock_dao.get_all.assert_called_once()

@patch('src.util.calculator.calculate_readiness')
def test_get_recipe_vegan_optimal(mock_calculate_readiness, controller, mock_dao):
    mock_dao.get_all.return_value = [
        {"name": "item1", "quantity": 5},
        {"name": "item2", "quantity": 3}
    ]
    controller.recipes = [
        {"name": "recipe1", "diets": ["vegan"], "ingredients": {"item1": 1, "item2": 2}},
        {"name": "recipe2", "diets": ["vegan"], "ingredients": {"item1": 5, "item2": 3}}
    ]
    mock_calculate_readiness.side_effect = [0.5, 1.0]

    result = controller.get_recipe(Diet.VEGAN, take_best=True)

    assert result["name"] == "recipe2"
    mock_dao.get_all.assert_called_once()

@patch('src.util.calculator.calculate_readiness')
def test_get_recipe_vegan_random(mock_calculate_readiness, controller, mock_dao):
    mock_dao.get_all.return_value = [
        {"name": "item1", "quantity": 5},
        {"name": "item2", "quantity": 3}
    ]
    controller.recipes = [
        {"name": "recipe1", "diets": ["vegan"], "ingredients": {"item1": 1, "item2": 2}},
        {"name": "recipe2", "diets": ["vegan"], "ingredients": {"item1": 5, "item2": 3}}
    ]
    mock_calculate_readiness.side_effect = [0.5, 1.0]

    result = controller.get_recipe(Diet.VEGAN, take_best=False)

    assert result["name"] in ["recipe1", "recipe2"]
    mock_dao.get_all.assert_called_once()
