class Car:
    # конструктор/инициализатор
    def __init__(self, color , model ): # self - обращение к обьекту (можно написать что угодно но так принято...)
        self.color = color
        self.model = model
    def drive_to(self, destination):
        print(f'in drive_to {destination}')
        print(f"Машина модели: {self.model} едет в {destination}")
    # pass #pass(пропустить) можно заменить на "..."

# инициализация обьектов
car1 = Car('черный','BMW')  # обьекты
car2 = Car('белый', 'Марк2')  # обьекты

print(car1)
print(car2)
print(type(car1))
print(car1.color , car1.model)
print(car2.color , car2.model)
car2.drive_to('Столб')

