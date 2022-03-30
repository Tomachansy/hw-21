class Request:
    def __init__(self, str):
        req = self.get_request(str)

        self.from_ = req[4]
        self.to_ = req[6]
        self.amount = int(req[1])
        self.product = req[2]

        if len(req) < 6:
            print("Ошибка при заполнении формы!")

    def get_request(self, str):
        return str.split(" ")

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to_}"
