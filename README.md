# Simple-flask-shop

Simple-flask-shop это интернет-магазин, разработанный при использовании фреймворка [Flask](https://flask.palletsprojects.com/en/1.1.x/). HTML-шаблоны были разработаны при помощи [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) и [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/). В качестве СУБД была использована технология [SQLite](https://sqlite.org/docs.html) + [SQLAlchemy](https://docs.sqlalchemy.org/en/14/).

## Installation

Используйте менеджер установки пакетов [pip](https://pip.pypa.io/en/stable/) для установки simple-flask-shop.

```bash
pip clone https://github.com/Dan1van/simple-flask-shop.git
pip install -r requirements.txt
```

## Usage

Запустите **run.py** и перейдите по адресу: http://127.0.0.1:5000/.

![Главная страница сайта](https://user-images.githubusercontent.com/40074918/92633391-62f1e100-f2db-11ea-91c5-2ce6845dd59b.png)

Если Вы увидите данную страницу, то запуск веб-сервера произошел успешно.

_____
Чтобы добавить новые товары в каталог, перейдите по ссылке: http://127.0.0.1:5000/create и заполните форму.

![Форма для добавления нового товара](https://imgur.com/NOTwIyl)
