import pytest
import requests
from selenium import webdriver

from curl import *
from user_methods import UserMethods
from generators import generate_email, UserGenerator


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(MAIN_SITE)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(MAIN_SITE)
    yield driver
    driver.quit()

@pytest.fixture
def random_email():
    return generate_email()

@pytest.fixture
def registered_user():
    """Фикстура для регистрации и удаления тестового пользователя"""
    user_data = UserGenerator.random_user()
    response = UserMethods.register(user_data)
    assert response.status_code == 200
    response_data = response.json()
    token = response_data['accessToken']

    yield {
        'email': user_data['email'],
        'password': user_data['password'],
        'name': user_data['name'],
        'token': token
    }

    # Cleanup - удаление пользователя после теста
    delete_response = UserMethods.delete_user(token)
    assert delete_response.status_code == 202

@pytest.fixture
def auth_token(registered_user):
    """Фикстура для получения токена авторизации"""
    return registered_user['token']