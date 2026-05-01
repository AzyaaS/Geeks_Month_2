# Родительский класс
class Car:
    # конструктор/инициализатор
    def __init__(self, color , model ): # self - обращение к обьекту (можно написать что угодно но так принято...)
        self.color = color
        self.model = model
        self.max_speed = 0
    def drive_to(self, destination):
        print(f"Машина модели: {self.model} едет в {destination}")
    # pass #pass(пропустить) можно заменить на "..."
    def change_color(self, new_color):
        self.color = new_color

# инициализация обьектов
car1 = Car('черный','BMW')  # обьекты
car2 = Car('белый', 'Марк2')  # обьекты

# дочерний класс, наследник, подкласс
class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model) # это обращение к методу из родительского класса
        self.number = number
    def drive_to(self, destination):
        super().drive_to(destination) # это обращение к методу из родительского класса
        print(f'Автобус номер {self.number} едет в рейс в {destination}')
class Truck(Car):
    def change_color(self, new_color):
        self.color = new_color
        print(f'цвет грузовика изменился на {new_color}')
car2.drive_to('Столб')
bus_42 = Bus('зеленый','Mercedes', 42)
print(bus_42.color, bus_42.model, bus_42.number)
bus_42.drive_to('Сокулук')

truck_1 = Truck('красный','lamborghini')
print(truck_1.color, truck_1.model)
truck_1.change_color('Синий')
print(truck_1.color, truck_1.model)

vehicles = [car2, truck_1, bus_42]
for v in vehicles:
    v.drive_to('Каракол')