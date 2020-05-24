from components.feeds import ComponentStatRepository


class QuestionStatRepository:

    def __init__(self, request, **kwargs):
        self._request = request
        self._question = kwargs.pop("question", None)
        self._components = kwargs.pop("components", None)
        self._test_unique = kwargs.pop("test_unique", None)

    def add_true(self):
        components = list()

        for component in self._components:

            csr = ComponentStatRepository(
                request=self._request,
                component=component,
                question=self._question,
                test_unique=self._test_unique
            )

            true_components = csr.add_true_answer()
            components.append(component.id)

            for true_component in true_components:
                components.append(true_component)

        return components

    def add_false(self):
        components = list()

        for component in self._components:

            csr = ComponentStatRepository(
                request=self._request,
                component=component,
                question=self._question,
                test_unique=self._test_unique
            )

            csr.add_false_answer()

            # soru parçasını doğru soru parçası listesine ekleyelim
            components.append(component.id)

        return components

    def add_empty(self):
        components = list()

        for component in self._components:

            csr = ComponentStatRepository(
                request=self._request,
                component=component,
                question=self._question,
                test_unique=self._test_unique
            )

            csr.add_empty_answer()

            # soru parçasını doğru soru parçası listesine ekleyelim
            components.append(component.id)

        return components


