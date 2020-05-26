class TestUniqueMixin:
    _test_unique = None

    @property
    def test_unique(self):
        return self._test_unique

    @test_unique.setter
    def test_unique(self, value):
        self._test_unique = value
