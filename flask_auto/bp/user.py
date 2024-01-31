

from flask import  Blueprint,current_app,request,jsonify,make_response,g
from io import BytesIO
import base64

from flask_auto import db
from flask_auto.models.user import User
from flask_auto.utils.tokenrequired import token_required
from flask_auto.utils.verccode import VercCode
from flask_auto.utils.apicode import ApiCode
from flask_auto.utils.validparams import validParams

user_blueprint = Blueprint("user_blueprint",__name__,url_prefix="/api/user")


@user_blueprint.route("/users",methods=['get'])
@token_required
def getUsers(current_user):
    users = User.query.filter_by(id=current_user.id).all()
    users_json=[ user.to_json() for user in users]
    return jsonify({"msg":"ok","data":users_json}),200


@user_blueprint.route("/login",methods=['post'])
def login():
    request_params = request.get_json()
    #必须要带请求参数
    valid_params = ['username','password']
    valid_params_msg = validParams(valid_params=valid_params,request_params=request_params)
    if valid_params_msg:
        return jsonify(valid_params_msg)

    verifycode_from_config = current_app.config.get("vericode")
    """
    if (verifycode_from_config.get("verifycodeid") == verifycodeid) and (verifycode_from_config.get("vericode").lower() != vericode):
        return jsonify({"msg": "vericodeFail"}), 200
    """
    user = User.query.filter_by(username=request_params.get("username")).first()

    if user is None:
        return jsonify(ApiCode.userNotExist()), 200

    if user.check_user_password(request_params.get("password")):
        for item in current_app.config['users']:
            if item['user_id'] == user.id:
                pass
                #return jsonify({"msg": "loginRepeated"}), 200
        auth_token= user.encode_user_token()
        current_app.config['users'].append({'user_id':user.id,'auth_token':auth_token})
       # current_app.config['users']['user_id'] = auth_token
        return jsonify(ApiCode.loginSuccess(data=[{"auth_token":auth_token}])), 200
    else:
        return jsonify(ApiCode.passwordIncorrect()),200


@user_blueprint.route("/logout",methods=['post'])
@token_required
def logout(current_user):
    data = request.get_json()
    user_id = current_user.id
    for item in current_app.config['users']:
        if item['user_id'] ==user_id:
            current_app.config['users'].remove(item)
            return jsonify(ApiCode.logoutSuccess())
    return jsonify(ApiCode.logoutSuccess())



@user_blueprint.route("/users",methods=['post'])
def createUsers():
    data = request.get_json()
    request_params = ['username']
    if request_params.sort() != [item for item in data.keys()].sort():
        return jsonify(ApiCode.paramsIncomplete()), 403
    user=User(username=data.get("username"),password=data.get("password"))
    db.session.add(user)
    db.session.commit()
    return jsonify(ApiCode.createUsersSuccess()),200

@user_blueprint.route("/getverifycode",methods=['post'])
def getVerifyCode():
    image, vercode = VercCode.generate_vercode()
    buffer = BytesIO()
    image.save(buffer, "png")
    buffer_str = buffer.getvalue()
    verifycodeimg = base64.b64encode(buffer_str).decode()
    current_app.config["vericode"] = {"verifycodeid":request.get_json().get("verifycodeid"),"vericode":vercode}
    return jsonify(ApiCode.getVerifyCodeSuccess(data={"data":{"verifycodeimg":verifycodeimg}})),200