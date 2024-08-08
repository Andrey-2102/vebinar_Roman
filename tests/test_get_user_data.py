import requests
import allure

from jsonschema import validate
from core.contracts import USER_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_USERS = "/api/users?page=2"
EMAIL = "@reqres.in"

@allure.title("Проверка получения списка")
def test_list_users():
    with allure.step("Запрос по адресу получения списка"):
        response = requests.get(BASE_URL + LIST_USERS)
        print(response.text)
    with allure.step("Получение списка осуществляется успешно"):
        assert response.status_code == 200

    data = response.json()["data"]
    for element in data:
        with allure.step("Проверка элементов списка"):
            validate(element, USER_DATA_SCHEME)
            with allure.step("Проверка окончания адреса почты"):
               assert element["email"].endswith(EMAIL)