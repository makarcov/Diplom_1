class TestBun:

    def test_bun_name_true(self, bun):
        assert bun.name == 'bun'

    def test_bun_price_true(self, bun):
        assert bun.price == 50

    def test_get_name_success(self, bun):
        assert bun.get_name() == 'bun'

    def test_get_price_success(self, bun):
        assert bun.get_price() == 50
