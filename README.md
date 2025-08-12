Автор:
- @arhside3
Контакты:
[Крещенский Богдан](https://t.me/arhside3)

Техно-стек:
- nginx 
- javascript 
- python 
- django 
- djangorest 
- postgres 
- docker

Как запустить проект на локальной машине с помощью Docker
- Клонирование репозитория
```
git clone https://github.com/arhside3/V2-HAKATON.git
```
- В корневой папке проекта вызовите команду Docker compose up
```
docker compose up
```
- Выполните миграцию базы данных в запущенном контейнере бэкенда
```
docker compose exec backend python manage.py migrate
```
- Сбор статических файлов для панели администратора Django
```
docker compose exec backend python manage.py collectstatic
```
- Скопируйте эти файлы в целевую папку, связанную с томом Docker
```
docker compose exec backend cp -r /app/collected_static/. /static/
```
