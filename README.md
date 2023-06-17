# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние"
Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска.

# Как установить

Скрипт совместим с Phyton с установленным фреймовком django и библиотеками psycopg2-binary и python-dotenv.<br/> 
Зависимости находятся в файле "requirements.txt"<br/>
Код запускается командой:<br/> `python manage.py runserver 0.0.0`

# Цель проекта
Код написания исследования на онлайн-курсе для веб-разработчиков dvmn.org .

# Что должно отображаться в браузере
На странице http://127.0.0.1:8000 вы должны  увидитеть список активных карт доступа с кодами пропуска и датой их регистрации.

# Файл .env
В файле .env храняться следующие настройки:

Настрокий базы данныхЖ
DATABASES_ENGINE = 'django.db.backends.postgresql_psycopg2'
DATABASES_HOST = 'checkpoint.devman.org'
DATABASES_PORT = '5434'
DATABASES_NAME = 'checkpoint'
DATABASES_USER = 'guard'
DATABASES_PASSWORD 

SECRET_KEY 

DEBUG = false

ALLOWED_HOSTS = localhost
