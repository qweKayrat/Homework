class Car:
    def __init__(self, name_model, age, vendor, power, color, price):
        if Car.__check_string(name_model) and Car.__check_digits(age) and Car.__check_string(vendor) and Car.__check_digits(
                power) and Car.__check_string(color) and Car.__check_digits(price):
            self.name_model = name_model
            self.age = age
            self.vendor = vendor
            self.power = power
            self.color = color
            self.price = price
        else:
            print("Вы ввели некорректные данные об автомобиле")

    def __check_digits(digit):
        if isinstance(digit, int) or isinstance(digit, float):
            return True
        else:
            return False

    def __check_string(s):
        if isinstance(s, str):
            return True
        else:
            return False

    def input_info_car(self):
        print(" Персональные данные ".center(30, "*"))
        print(f"""Название модели: {self.name_model}
Год выпуска: {self.age}
Производитель: {self.vendor}
Мощность двигателя: {self.power} л.с.
Цвет машины: {self.color}
Цена: {self.price} руб""")
        print("=" * 30)

    def set_name_model(self, new_name):
        if Car.__check_string(new_name):
            self.name_model = new_name
        else:
            print("Модель машины должна быть строкой")

    def get_name_model(self):
        return self.name_model

    def set_age(self, new_age):
        if Car.__check_digits(new_age):
            self.age = new_age
        else:
            print("Год выпуска должен являться числом")

    #   Сделал Setter для введённого параметра
    def set_param(self, param):
        match param:
            case 'name':
                value = input("Введите название автомобиля: ")
                self.name_model = value
            case 'age':
                value = int(input("Введите год выпуска автомобиля: "))
                self.age = value
            case 'vendor':
                value = input("Введите производителя автомобиля: ")
                self.vendor = value
            case 'power':
                value = int(input("Введите мощность автомобиля: "))
                self.power = value
            case 'color':
                value = input("Введите цвет автомобиля: ")
                self.color = value
            case 'price':
                value = int(input("Введите цену автомобиля: "))
                self.price = value
            case _:
                print("Вы ввели номер параметра который не существует")

    #   Сделал Getter для введённого параметра
    def get_param(self, param):
        match param:
            case 'name':
                return self.name_model
            case 'age':
                return self.age
            case 'vendor':
                return self.vendor
            case 'power':
                return self.power
            case 'color':
                return self.color
            case 'price':
                return self.price
            case _:
                print("Вы ввели номер параметра который не существует")

    def get_age(self):
        return self.age

    def set_vendor(self, new_vendor):
        if Car.__check_string(new_vendor):
            self.vendor = new_vendor
        else:
            print("Наименование продавца автомобиля не может быть числом!")

    def get_vendor(self):
        return self.vendor

    def set_power(self, new_power):
        if Car.__check_digits(new_power):
            self.power = new_power
        else:
            print("Мощность машины не может быть строкой")

    def get_power(self):
        return self.power

    def set_color(self, new_color):
        if Car.__check_string(new_color):
            self.color = new_color
        else:
            print("Цвет машины должен быть строкой")

    def get_color(self):
        return self.color

    def set_price(self, new_price):
        if Car.__check_digits(new_price):
            self.price = new_price
        else:
            print("Цена автомобиля должна быть числом")

    def get_price(self):
        return self.price


car1 = Car("X7 M50i", 2021, 'BMW', 530, 'white', 10790000)
car1.input_info_car()
car1.set_name_model("300 SLR Uhlenhaut Coupe")
print(car1.get_name_model())
car1.set_age(1955)
print(car1.get_age())
car1.set_vendor('Mercedes-Benz')
print(car1.get_vendor())
car1.set_power(310)
print(car1.get_power())
car1.set_color('silver')
print(car1.get_color())
car1.set_price(135_000_000 * 81)
print(car1.get_price())

car1.input_info_car()

car1.set_param('name')
print(car1.get_param('name'))
car1.input_info_car()
