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
