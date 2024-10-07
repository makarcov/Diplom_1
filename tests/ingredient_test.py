class TestIngredient:

    def test_ingredient_type_true(self, ingredient):
        assert ingredient.type == 'sauce'

    def test_ingredient_name_true(self, ingredient):
        assert ingredient.name == 'spicy'

    def test_ingredient_price_true(self, ingredient):
        assert ingredient.price == 20

    def test_get_type_success(self, ingredient):
        assert ingredient.get_type() == 'sauce'

    def test_get_name_success(self, ingredient):
        assert ingredient.get_name() == 'spicy'

    def test_get_price_success(self, ingredient):
        assert ingredient.get_price() == 20
