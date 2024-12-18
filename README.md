# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка
Как установить

## Как установить

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`

Также необходимо создать файл .env и добавить туда следующие значения:

```ENGINE=
HOST=
PORT=
NAME=
DB_USER=
PASSWORD=
SECRET_KEY=
```

## Как запустить

Чтобы запустить сайт, необходимо в командную строку вбить `python3 manage.py runserver`

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
