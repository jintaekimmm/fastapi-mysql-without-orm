from databases import Database
from app.env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

db_conn_string = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
)

database = Database(db_conn_string, min_size=5, max_size=20)
