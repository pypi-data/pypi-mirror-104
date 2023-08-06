import os

def create_gitignore():
    with open('.gitignore', 'w') as f:
        ignore_text = """\
venv
**/__pycache__
site.db
migrations/versions/**/*
*.env
.env
"""
        f.write(ignore_text)

def create_app_py(name):
    def wrapper():
        with open('app.py','w') as f:
            app_py_text = f"""\
from {name} import app

if __name__=='__main__':
    app.run(debug=True)            
"""
            f.write(app_py_text)
    return wrapper

def create_env():
    with open('.env','w') as f:
        env_text = f"""\
SQLALCHEMY_DATABASE_URI="sqlite:///../site.db"
SECRET_KEY={os.urandom(24).hex()}\
"""
        f.write(env_text)

def create_config_py():
    with open('config.py', 'w') as f:
        config_py_text = f"""\
from os import environ as env
class Config:
    SECRET_KEY = env.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI')
"""
        f.write(config_py_text)

def create_init_py(name):
    def wrapper():
        with open(os.path.join(name, '__init__.py'), 'w') as f:
            init_py_text = """\
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app=Flask(__name__)

app.config.from_object(Config)

db=SQLAlchemy(app)

migrate=Migrate(app, db)
""" 
            f.write(init_py_text)
    return wrapper

def create_static_folders(name):
    def wrapper():
        os.mkdir(os.path.join(name, 'static'))
        os.mkdir(os.path.join(name, 'static', 'js'))
        os.mkdir(os.path.join(name, 'static', 'css'))
        os.mkdir(os.path.join(name, 'static', 'images'))
    return wrapper