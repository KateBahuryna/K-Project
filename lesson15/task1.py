# Создать класс Contact, у которого должны быть
# атрибуты email, phone, first_name, last_name
# Сделать валидации, что email - строка, содержащая с
# имвол @ и правая часть находится в списке из:
# gmail.com, yandex.ru, ya.ru, yahoo.com
#
# phone - номер телефона начинается с символа +,
# код страны находится в списке
# 375, 48, 374
#
# first_name, last_name - строки, начинающиеся с
# большой буквы и длиной от 5 до 15  символов
#
# Все проверки реализовать через property

class Contact:
    def __init__(self, email, phone, first_name, last_name):
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name

    def _validate_email(self, value):
        if '@' not in value:
            raise ValueError("Email must contain symbol @.")

        email_split = value.split('@')
        if email_split[1] not in ['gmail.com', 'yandex.ru', 'ya.ru',
                                  'yahoo.com']:
            raise ValueError("Unsupported email provider.")

    def _validate_phone(self, value):
        if value[0] != '+':
            raise ValueError("The phone number should be started from +.")

        if not (value[1:4] in ['375', '374'] or value[1:3] == '48'):
            raise ValueError("Unsupported mobile provider.")

    def _validate_name(self, value):
        if not value[0].isupper():
            raise ValueError("Name should start from capital letter.")

        if len(value) not in range(5, 15):
            raise ValueError("Name length must be in range (5, 15).")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._validate_email(value)
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._validate_phone(value)
        self._phone = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._validate_name(value)
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._validate_name(value)
        self._last_name = value


c1 = Contact('ebogurina@gmail.com', "+487298675690", 'Vahuryna', 'Katsiaryna')
print(c1)
