from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# 初始化数据库
db.init_app(app)

@app.before_first_request
def create_tables():
    if app.config["ENV"] == "development":  # 仅在开发环境中创建表
        db.create_all()

@app.route('/api/login', methods=['POST'])
def login():
    """
    登录接口
    """
    data = request.json
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"code": 1, "message": "Invalid input", "data": None}), 400

    username = data["username"]
    password = data["password"]

    # 查询用户
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        # 登录成功，生成 token
        token = str(uuid.uuid4())
        # 可以选择保存 token
        user.token = token
        db.session.commit()
        return jsonify({
            "code": 0,
            "message": "Login successful",
            "data": {
                "token": token
            }
        }), 200
    else:
        # 登录失败
        return jsonify({
            "code": 1,
            "message": "Invalid username or password",
            "data": None
        }), 401

@app.route('/api/register', methods=['POST'])
def register():
    """
    注册接口
    """
    data = request.json
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"code": 1, "message": "Invalid input", "data": None}), 400

    username = data["username"]
    password = data["password"]

    # 检查用户名是否已存在
    if User.query.filter_by(username=username).first():
        return jsonify({"code": 1, "message": "Username already exists", "data": None}), 400

    try:
        # 创建新用户
        hashed_password = generate_password_hash(password)  # 生成加密后的密码
        new_user = User(username=username, password=hashed_password)  # 设置用户名和加密密码
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"code": 0, "message": "Registration successful", "data": None}), 201

    except Exception as e:
        db.session.rollback()  # 回滚事务
        app.logger.error(f"Error during registration: {str(e)}")  # 记录异常信息到日志
        return jsonify({"code": 1, "message": "Registration failed due to an internal error", "data": None}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)