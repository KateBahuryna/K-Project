# ЗАДАНИЕ 2
# Создать класс Message, который принимает атрибут
# text, который является текстом
# какого-то сообщения. Также в инициализаторе у класса
# задать атрибут created_at, в который
# сохранить текущий timestamp (unix time)
# Создать класс Song, который принимает два атрибута:
# name - название песни и author - автор песни
# Также в инициализаторе у класса задать атрибут created_at, в
# который сохранить текущий timestamp (unix time)
#
# Создать класс-дескриптор Censored, который будет валидировать
# поля name и text у этих классов.
# Правило валидации: если в тексте сообщения или названии песни
# найдётся слово fuck (в любом регистре),
# то перед присваиванием этого текста атрибуту класса, дескриптор
# заменяет это слово на ****
#
# Пример структуры программы:
#
# class Censored:
#
# # Тут реализовать протокол дескриптора
#
# class Song:
#     name = Censored()
#
#     def __init__(self, name, author):
#         self.name = name
#         self.author = author
#         # также добавить created_at
#
#
# class Message:
#     text = Censored()
#
#     def __init__(self, text):
#         self.text = text
#         # также добавить created_at
#
#
# m1 = Message("Fuck sofof")
# print(m1.text)  # Выведет "**** sofof"
#
# m2 = Message("Hello World")
# print(m2.text)  # Выведет  "Hello World"
import time


class Censored:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        text = []
        print(type(value))
        for world in value.split():
            if world.lower() == 'fuck':
                text.append(world.lower().replace('fuck', '****'))
            else:
                text.append(world)
        setattr(instance, self.name, ' '.join(text))


class Message:
    text = Censored()

    def __init__(self, text):
        self.text = text
        self.created_at = time.time()
        # self.created_at = created_at


class Song:
    name = Censored()

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.created_at = time.time()
        # self.created_at = created_at


m1 = Message('FUCK fuck hello')
print(m1.text)

s1 = Song('fuck lalala', 'HE')
print(s1.name)
print(s1.created_at)
