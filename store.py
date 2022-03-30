from storage import Storage


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, value):
        if self.get_free_space() >= value:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + value
                    print(f"Добавлено {value} {name}! Осталось мест {self.get_free_space()}.")
            if name not in self.items:
                self.items[name] = value
                print(f"Добавлено {value} {name}! Осталось мест {self.get_free_space()}.")
        elif self.get_free_space() < value:
            print(f"Недостаточно мест (осталось: {self.get_free_space()}).")

    def remove(self, name, value):
        for key in self.items.keys():
            if name == key:
                if self.items[key] - value >= 0:
                    self.items[key] = self.items[key] - value
                else:
                    print(f"{name.title()} не хватает на складе(осталось {self.items[key]}), "
                          f"попробуйте уменьшить количество.")
            elif name not in self.items:
                print(f"{name.title()} нет на сладе.")

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())
