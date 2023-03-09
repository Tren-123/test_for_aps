# Тестовое задание - API с методами search, delete
Версия python для гарантированной работы проекта >= 3.10.6

Для запуска проекта на локальном компьютере(OS Linux):

1. Клонируйте репозиторий
```
$ git clone https://github.com/Tren-123/test_for_aps
```
2. Скачайте базу данных sqllite https://disk.yandex.ru/d/RokGWuuHsQpZcA и добавьте в родительскую директорию проекта

3. Создайте и запустите виртуальное окружение
```
$ python3 -m venv venv
$ source venv/bin/activate
```
4. Установите необходимые пакеты
```
$ pip install -r requrements.txt
```
5. В settings.py укажите необходимые настройки для подключения к elastic cloud

6. Запустите сервер
```
$ uvicorn main:app
```

Документация к API доступна по ссылке http://localhost:8000/docs