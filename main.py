from request import Request
from shop import Shop
from store import Store

if __name__ == '__main__':

    shop = Shop()
    print("Магазин:")
    shop.add("печеньки", 4)
    shop.add("собачки", 3)
    shop.add("котики", 5)
    shop.add("зефирки", 1)
    print("----------------------------------------")
    store = Store()
    print("Склад:")
    store.add("зефирки", 5)
    store.add("клей", 4)
    store.add("котики", 1)
    store.add("печеньки", 5)

    user = input()
    user_req = user.split(" ")

    try:
        user_req[1] = int(user_req[1])
    except:
        print("Введите число!")

    if ("Доставить" and "из" and "в" and "склад" and "магазин") not in user_req:
        print("Введите информацию по шаблону 'Доставить (количество товара) (название товара) из (склад) в (магазин)'")

    else:
        req = Request(user)
        print(req)

        if "магазин" in req.to_ and "склад" in req.from_:
            if req.product in store.get_items():
                if req.amount <= store.get_items()[req.product]:
                    if req.product not in shop.get_items() or \
                            shop.get_limit - int(shop.get_items()[req.product] + req.amount) >= 0:
                        print(f"\nНужное количество есть на складе\n")
                        print(f"Курьер забрал {req.amount} {req.product} со {req.from_}")
                        print(f"Курьер везет {req.amount} {req.product} со {req.from_} в {req.to_}")

                        if sum(shop.get_items().values()) + int(req.amount) < shop.capacity:
                            print(f"Курьер доставил {req.amount} {req.product} в {req.to_}\n")
                            store.remove(req.product, req.amount)
                            shop.add(req.product, req.amount)

                            print(f"\nНа складе хранится:")
                            for key, value in store.items.items():
                                print(key, value)

                            print(f"\nВ магазине хранится:")
                            for key, value in shop.items.items():
                                print(key, value)

                    else:
                        print("В магазине недостаточно места, попробуйте что то другое")
                else:
                    print("Не хватает на складе, попробуйте заказать меньше")
            else:
                print("Товар отсутствует на складе.")
        else:
            print("Доставка только из склада!")
