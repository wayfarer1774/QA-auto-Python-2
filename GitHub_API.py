import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение входных данных из загруженных переменных окружения
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

# Создание URL-адресов для работы с GitHub API
BASE_URL = "https://api.github.com"
REPO_URL = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Создание репозитория
def create_repository():
    url = f"{BASE_URL}/user/repos"
    data = {
        "name": REPO_NAME,
        "private": False
    }
    response = requests.post(url, json=data, headers=HEADERS)
    if response.status_code == 201:
        print(f"Репозиторий '{REPO_NAME}' успешно создан.")
    else:
        print(f"При создании репозитория возникла ошибка: {response.status_code}, {response.text}")

# Проверка наличия репозитория
def check_repository_exists():
    response = requests.get(REPO_URL, headers=HEADERS)
    if response.status_code == 200:
        print(f"Репозиторий '{REPO_NAME}' существует.")
        return True
    else:
        print(f"Репозиторий '{REPO_NAME}' не обнаружен.")
        return False

# Удаление существующего репозитория
def delete_repository():
    response = requests.delete(REPO_URL, headers=HEADERS)
    if response.status_code == 204:
        print(f"Репозиторий '{REPO_NAME}' удален.")
    else:
        print(f"При удалении репозитория возникла ошибка: {response.status_code}, {response.text}")

if __name__ == "__main__":
    create_repository()

    if check_repository_exists():
        delete_repository()