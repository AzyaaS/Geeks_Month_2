class Car:
    # конструктор/инициализатор
    def __init__(self, color , model="Mark"): # self - обращение к объекту (можно написать что угодно, но так принято...)
        self.color = color
        self.model = model
        self.__max_speed = 0
        self._fined = False

    def _calculated_fuel(self):
        print(self.color)
        return 1

    def drive_to(self, destination):
        if not self._calculated_fuel():
            print('нет топлива')
        print(f"Машина модели: {self.model} едет в {destination}, "
              f"Оштрафован: ", "да" if car1._fined else "нет")
    # pass #pass(пропустить) можно заменить на "..."
    def change_color(self, new_color):
        self.color = new_color
    # геттер(get) - для получения значения приватных атрибутов
    def get_max_speed(self):
        return self.__max_speed
    # сеттер(set - выставить значение) - для установки значения
    def set_max_speed(self, new_speed):
        if new_speed < 0:
            raise ValueError ("Новая скорость < 0")
        self.__max_speed = new_speed
    @property # property(свойство) - декоратор
    def max_speed(self):
        # геттер
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, new_speed):
        if new_speed < 0:
            raise ValueError ("Новая скорость < 0")
        self.__max_speed = new_speed

car1 = Car('черный', 'BMW')
car2 = Car('Белый')
print(car1.color, car1.model)
# print(car1.__max_speed) # ошибка
car1.drive_to('Кант')
print("Оштрафован: ", "да" if car1._fined else "нет")
car1._calculated_fuel()
car1.__max_speed = 200 # не настоящий  __max_speed из класса
# print(car2.__max_speed)
print("Car 1 max_speed: ", car1.get_max_speed())
car1.set_max_speed(180)
print(f"Car 1 max_speed: {car1.get_max_speed()}")
print(f"Car 1 max_speed: {car1.max_speed}")
car1.max_speed = 200
print(f"Car 1 max_speed: {car1.max_speed}")