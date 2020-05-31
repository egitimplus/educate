class TestUniqueMixin:
    __test_unique = None

    @property
    def test_unique(self):
        return self.__test_unique

    @test_unique.setter
    def test_unique(self, value):
        self.__test_unique = value
