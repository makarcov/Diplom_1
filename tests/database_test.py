import pytest


class TestDatabase:

    @pytest.mark.parametrize('buns', ['black bun', 'white bun', 'red bun'])
    def test_database_buns_success(self, database, buns):
        buns_names = []
        for i in range(len(database.buns)):
            name = database.buns[i].name
            buns_names.append(name)
        assert buns in buns_names

    @pytest.mark.parametrize('ingredients', ['hot sauce', 'sour cream', 'chili sauce', 'cutlet', 'dinosaur', 'sausage'])
    def test_database_ingredients_success(self, database, ingredients):
        ingredients_names = []
        for i in range(len(database.ingredients)):
            name = database.ingredients[i].name
            ingredients_names.append(name)
        assert ingredients in ingredients_names

    def test_available_buns_success(self, database):
        assert len(database.buns) == 3

    def test_available_ingredients_success(self, database):
        assert len(database.ingredients) == 6