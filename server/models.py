from flask_sqlalchemy import SQLAlchemy

# 初始化 SQLAlchemy
db = SQLAlchemy()

# 用户模型
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)