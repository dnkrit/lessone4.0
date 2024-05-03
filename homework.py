class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f'Товар {item_name} был добавлен в {self.name}')

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f'Товар {item_name} удален из {self.name}')

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f'Цена на товар {item_name} обновлена в {self.name}')
        else:
            print(f'Товар {item_name} не найден')

store1 = Store('Шестерочка', 'Работаем на Толстого')
store2 = Store('Ночной заход', 'Ищи на карте Яндекс')
store3 = Store('Бабкинрай', 'Рядом с аптекой')

store1.add_item('Сыр с плесенью', 300)
store2.add_item('Пиво', 100)
store3.add_item('Хлеб', 50)

store2.update_price('Пиво', 150)