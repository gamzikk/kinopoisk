# kinopoisk

kinopoisk - веб приложение с каталогом фильмов, регистрацией и авторизацией пользователей, с системами премиум-подписок, рейтинга, комментариев.

# Руководство по запуску

+ Клонируйте репозиторий
+ Создайте виртуальное окружение и активируйте его:

#### Windows
```
python -m venv .venv
.venv\Scripts\activate
```

#### Linux
```
python3 -m venv .venv
source .venv/bin/activate
```

+ Установите зависимости:

```
pip install -r requirements.txt
```

+ На вашей операционой системе должен быть установлен PostgreSQL
+ Создайте базу данных kinopoisk_db в PotgreSQL
+ Проведите миграции командой:

#### Windows
```
python manage.py migrate
```

#### Linux
```
python3 manage.py migrate
```

+ Создайте суперпользователя для входа в админ панель:

#### Windows
```
python manage.py createsuperuser
```

#### Linux
```
python3 manage.py createsuperuser
```