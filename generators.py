import random
import string

from faker import Faker

fake = Faker()

def generate_email():
    return fake.email()


class UserGenerator:
    @staticmethod
    def random_user():
        """Генерация случайного пользователя"""
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return {
            "email": f"test_{random_str}@example.com",
            "password": "password123",  # Стандартный пароль для тестов
            "name": f"Test User {random_str}"
        }