import json

import requests

from curl import Url


class UserMethods:
    @staticmethod
    def register(body):
        """Регистрация нового пользователя"""
        response = requests.post(Url.BASE_URL + Url.REGISTER, json=body)
        if response.status_code == 200 and 'accessToken' in response.json():
            data = response.json()
            if data['accessToken'].startswith('Bearer '):
                data['accessToken'] = data['accessToken'][7:]
            response._content = json.dumps(data).encode()
        return response

    @staticmethod
    def delete_user(token):
        """Удаление пользователя"""
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        return requests.delete(Url.BASE_URL + Url.USER, headers=headers)