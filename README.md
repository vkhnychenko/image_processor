# Тестовое задание для backend разработчика

## Описание

Сервис, который позволяет загружать изображения с компьютера пользователя, или по ссылке, а затем изменять их размер.
Тестовый запуск сервиса на локальном компьютере происходит при помощи Docker

## Использованные технологии
* Python
* Django
* Docker

## Запуск проекта
Установить:

* [docker](https://www.digitalocean.com/community/tutorials/docker-ubuntu-18-04-1-ru)
* [docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04-ru)

Создать файл `.env` с настройками:
* `DEBUG=1`
* `SECRET_KEY=secretkey`
* `DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]`

Выполнить команду:
* `$docker-compose up --build`

