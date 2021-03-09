import os

APP_ENV = os.environ.get("APP_ENV", "development")

DB_USER = os.environ.get("MYSQL_USER")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD")
DB_HOST = os.environ.get("MYSQL_HOST")
DB_PORT = os.environ.get("MYSQL_PORT")
DB_NAME = os.environ.get("MYSQL_DATABASE")
