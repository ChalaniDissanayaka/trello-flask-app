python3 -m venv .venv

source .venv/bin/activate

pip3 install psycopg2-binary flask_sqlalchemy flask_marshmallow marshmallow_sqlalchemy
flask_bcrypt flask_jwt_extended

pip3 freeze > requirements.txt

conect to database :- psql comand

create a database - CREATE DATABASE trello_db;
set the password - CREATE USER trello_dev WITH PASSWORD '123456';
Grant the database - GRANT ALL PRIVILEGES ON DATABASE trello_db TO trello_dev ;
Grant the database - GRANT ALL ON SCHEMA public TO trello_dev ;
connect to database - \c trello_db

in init.py create connection - app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://trello_dev:123456@localhost:5432/trello_db"

\q - to quite to the psql
exit() - to quite to the sql

And make sure your file structure is correct:

trello/
├── .venv/
├── main.py
├── init.py
├── .env
├── .flaskenv
└── ...
