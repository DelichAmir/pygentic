import random
from typing import List
from dataclasses import dataclass
from pydantic import EmailStr, constr, parse_obj_as


@dataclass
class User:
    first_name: str
    last_name: str
    age: int
    email: EmailStr
    phone: constr(regex=r'^\+7\d{10}$')


class DataGenerator:
    @staticmethod
    def first_name() -> str:
        first_names = ['Alexey', 'Vasiliy', 'Dmitriy', 'Elena', 'Irina', 'Natalia', 'Sergey']
        return random.choice(first_names)

    @staticmethod
    def last_name() -> str:
        last_names = ['Smirnov', 'Ivanov', 'Kuznetsov', 'Petrov', 'Sokolov', 'Mikhailov', 'Novikov']
        return random.choice(last_names)

    @staticmethod
    def age() -> int:
        return random.randint(18, 60)

    @staticmethod
    def email(first_name: str, last_name: str) -> EmailStr:
        domains = ['gmail.com', 'yandex.ru', 'mail.ru', 'list.ru', 'protonmail.com']
        email_str = f"{first_name.lower()}.{last_name.lower()}.{random.randint(1, 100)}@{random.choice(domains)}"
        return parse_obj_as(EmailStr, email_str)

    @staticmethod
    def phone() -> str:
        return f"+7{random.randint(9000000000, 9999999999)}"


def random_user_data_generator() -> User:
    first_name = DataGenerator.first_name()
    last_name = DataGenerator.last_name()
    age = DataGenerator.age()
    email = DataGenerator.email(first_name, last_name)
    phone = DataGenerator.phone()

    return User(first_name=first_name, last_name=last_name, age=age, email=email, phone=phone)


def generate_users_list(n: int) -> List[User]:
    return [random_user_data_generator() for _ in range(n)]


# Generating a list of 10 random users
users = generate_users_list(10)
for user in users:
    print(user)
