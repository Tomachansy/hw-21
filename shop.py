from store import Store


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.items = {}
        self.capacity = 20
        self._limit = limit

    @property
    def get_limit(self):
        return self._limit

    def add(self, name, value):
        if value <= self.get_limit:
            super().add(name, value)
        else:
            print(f"Мест для {name} нет.")

