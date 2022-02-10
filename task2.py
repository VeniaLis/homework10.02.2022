#Создайте класс Human.

class Human:
#Определите для него два статических поля: default_name и default_age.

    default_name = 'Venia'
    default_age = 31

#задайте значения по умолчанию, используя свойства default_name и default_age.
    def __init__(self, name=default_name, age=default_age):
        self.name = name  #Публичные - name и age
        self.age = age

        #Приватные - money и house.

        self.__money = 15000
        self.__house = None

# Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.

    def info(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')
        print(f'money: {self.__money}')
        print(f'house: {self.__house}')

# Реализуйте справочный статический метод default_info(), который будет выводить статические поля
# default_name и default_age.

    @staticmethod
    def default_info():
       print(f'default_name: {Human.default_name}')
       print(f'default_age: {Human.default_age}')

       # Реализуйте приватный метод make_deal(),
    def __make_deal(self, house, price):
        self.__money -= price   # покупки дома: уменьшать количество денег
                                # на счету и присваивать ссылку на только что купленный дом.

        self.__house = house

# Реализуйте метод earn_money(), увеличивающий значение свойства money.
    def earn_money(self, amount):
        self.__money += amount
        print(f'Earn {amount} money, current value: {self.__money}')

# Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и
# совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры
# метода: ссылка на дом и размер скидки
    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('not enough money')


# 1. Создайте класс House

class House:

# Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price.
    def __init__(self, area, price):
        self._area = area  # Свои начальные значения они получают из параметров метода __init__()
        self._price = price


#Создайте метод final_price(), который принимает в качестве
# параметра размер скидки и возвращает цену с учетом данной скидки.

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'final price: {final_price}')
        return final_price

# Создайте класс SmallHouse, унаследовав его функционал от класса House

class SmallHouse(House):


    area = 40  # Внутри класса SmallHouse переопределите метод __init__() так,

    def __init__(self, price): # чтобы он создавал объект с площадью 40м2
        super().__init__(SmallHouse.area, price)


#1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома:
# уменьшать количество денег на счету и присваивать ссылку на только что купленный дом.
# В качестве аргументов данный метод принимает объект дома и его цену.

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

#2. Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и совершать сделку.
# Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка на дом и размер скидки

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            print(f'You make it !!!, Congratulations')
        else:
            print('not enough money')

if __name__ == "__main__":

    Human.default_info()

    veniamin = Human('Venia', 31)
    veniamin.info()

    small_house = SmallHouse(45000)



    veniamin.earn_money(25000)
    veniamin.buy_house(small_house, 25)
