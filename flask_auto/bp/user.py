

from flask import  Blueprint,current_app,request,jsonify

from flask_auto import db
from flask_auto.models.user import User



user_blueprint = Blueprint("user_blueprint",__name__,url_prefix="/api/user")


@user_blueprint.route("/users",methods=['get'])
def getUsers():
    users = User.query.filter_by().all()
    users_json=[ user.to_json() for user in users]
    return jsonify({"user":users_json}),200


@user_blueprint.route("/login",methods=['post'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"msg": "faild"}), 404
    user = User.query.filter_by(username=data.get("username")).first()
    if not user:
        jsonify({"msg": "userNotExist"}), 200
    if user.check_user_password(data.get("password")):
        auth_token= user.encode_user_token()
        return jsonify({"msg": "loginSuccess","auth_token":auth_token}), 200
    else:
        return jsonify({"msg":"loginFailed"}),200

@user_blueprint.route("/users",methods=['post'])
def createUsers():
    data = request.get_json()
    if not data:
        return  jsonify({"msg":"faild"}),404
    user=User(username=data.get("username"),password=data.get("password"))
    db.session.add(user)
    db.session.commit()
    current_app.logger.info("ok")
    return jsonify({"msg":"ok"}),200