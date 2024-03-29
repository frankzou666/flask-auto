# _*_coding:utf-8 _*_


from flask import  Flask,redirect
from flask_sqlalchemy import SQLAlchemy
import  logging
import os
from flask_cors import CORS

from config import Config


db =  SQLAlchemy()
def registerLogging(app):
    app.logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(os.path.join(os.getcwd(), 'flask_auto/logs/flask_auto.log'),encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)



def registerBluepoint(app):
    from flask_auto.bp.user import user_blueprint
    from flask_auto.bp.index import index_blueprint
    from flask_auto.bp.server import server_blueprint
    app.register_blueprint(user_blueprint)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(server_blueprint)
    # app.register_blueprint(admin_blueprint)


def redirectTo404(e):
    return redirect("/"),301


def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    registerLogging(app=app)
    db.init_app(app=app)
    CORS().init_app(app=app)
    registerBluepoint(app)
    app.config['users']=[]
    app.register_error_handler(404, redirectTo404)

    return app