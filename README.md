# FastAPI - MySQL Without ORM 

 - Project Structure

```shell
app
├── __init__.py
├── core
│   └── db.py
├── cruds
│   ├── __init__.py
│   └── tweets.py
├── dependencies.py
├── env.py
├── main.py
├── routers
│   ├── __init__.py
│   └── tweets.py
└── schemas
    ├── __init__.py
    └── tweets.py
```

 - Installed Package
1. [FastAPI](https://fastapi.tiangolo.com/tutorial/#install-fastapi)
2. [Databases](https://www.encode.io/databases/#installation)

```shell
- pip install fastapi
- pip install uvicorn[standard]
- pip install databases[mysql]
```

 - Running
```shell
uvicorn app.main:app --reload --port=8000 --host=0.0.0.0
```
