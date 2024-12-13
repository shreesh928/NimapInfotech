Install:- pip install mysqlclient
If Facing Issue:
Install:- pip install mysql-connector-python

Create DB and provide name in settings.py I connected the mysql manually so we have to write a
db name, password, etc. if your db is working another port please change the port over there.

Make Migrations and migrate the model into db so that its reflect and create db tables:
python manage.py makemigrations
python manage.py migrate

Run The Django server:
use python manage.py runserver
