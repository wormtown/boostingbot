from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Storage.PostgreSQL.Config import Config
from Storage.Redis.RedisConfig import RedisConfig
from Api.AuthRoutes import auth_bp
from Api.ChatRoutes import chat_bp
from flask_redis import FlaskRedis
app = Flask(__name__)

#Postgresql初始化
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
#初始化SQLAlchemy
db = SQLAlchemy(app)
#初始化redis
app.config['REDIS_URL'] =RedisConfig.REDIS_URI
redis_store = FlaskRedis(app)
#蓝图接口注册
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(chat_bp, url_prefix='/chat')


if __name__ == '__main__':
    app.run(debug=True)