class User:
    # переменные(атрибуты) класса
    user_count = 0
    default_password = '123456789'
    # методы объекта
    def __init__(self,name,phone):
        # переменные(атрибуты) экземпляра(объекта)
        self.name = name
        self.phone = phone
        self.role = 'user'
        self.password = User.default_password
        User.user_count += 1

    def test(self):
        print(User.user_count, User.default_password)

    # методы класса
    @classmethod
    def create_admin(cls, name,phone):
        # для особенного создания объектов
        admin = cls(name,phone)
        admin.role = 'admin'
        admin.password = 'qwerty'
        print(cls.get_user_count())
        return admin

    @classmethod
    def get_user_count(cls):
        return cls.user_count
    # статические методы
    @staticmethod
    def validate_password(password):
        # для проверки длины пароля
        if len(password) < 8:
            return False
        else:
            return True
        # short version
        return len(password) >= 8
    def change_password(self, new_password):
        if not User.validate_password(new_password):
            raise ValueError('Пароль слишком короткий')
        self.password = new_password

print(f'Количество пользователей: {User.user_count}')
user1 = User('Azik', '500848654')
print(f'Количество пользователей: {User.user_count}')
user2 = User('Karina', '9935619356')
print(f'Количество пользователей: {User.user_count}')
user1.test()
user2.test()
print(f'Passwords: {user1.password},{user2.password}')
print(f'class attributes: {User.user_count}, {User.default_password}')
admin1 = User.create_admin('Rayimbek', '99600000')
print(f'admin user: {admin1.name}, {admin1.phone}, {admin1.role}, {admin1.password}')
print(f'User count: {User.get_user_count()}')
print(User.validate_password('xxxxxxxxx'))
user1.change_password('11111111')

