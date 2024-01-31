import random
import pyotp
from flask import  Blueprint,current_app,request,jsonify,make_response,g
import qrcode
import io
from flask_auto import db
from flask_auto.models.user import User
from flask_auto.utils.tokenrequired import token_required
from flask_auto.models.server import Server

server_blueprint = Blueprint("server_blueprint",__name__,url_prefix="/api/server")



@server_blueprint.route("/",methods=['get'])
def getServer():
    servers = Server.query.filter_by().all()
    servers_json=[ servers.to_json() for servers in servers]
    return jsonify({"msg":"ok","data":servers_json}),200


@server_blueprint.route("/",methods=['delete'])
def delServer():
    data = request.get_json()
    if not data.get("server_id"):
        return jsonify({"msg": "serveridIsNull"}), 200
    server = Server.query.filter_by(id=data.get("server_id")).first()
    if not server:
        return jsonify({"msg": "serverNotExist"}), 200
    else:
        db.session.delete(server)
        db.session.commit()
        current_app.logger.info("server_id:"+str(server.id)+" 已被删除")
        return jsonify({"msg":"ok"}),200




"""
@server_blueprint.route("/getauth",methods=['get'])
def getAuth():
    #这个密钥应该为每个用户生成一个
    SECRET_KEY = 'base32secret3232'
    totp = pyotp.totp.TOTP(SECRET_KEY)
    qr_image=qrcode.make(totp.provisioning_uri(name="063"))
    buffer = io.BytesIO()
    qr_image.save(buffer)
    buffer.seek(0)
    response = make_response(buffer.getvalue())
    response.mimetype = 'image/png'
    return  response
    #return response


@server_blueprint.route("/getgoogle",methods=['post'])
def getgoogle():
    #取用户的密钥
    SECRET_KEY = 'base32secret3232'
    #获取用户输入
    data = request.get_json()
    totp = pyotp.totp.TOTP(SECRET_KEY)
    google_verify_result= totp.verify(data.get("key"))
    if google_verify_result:
        return  jsonify({"msg":"google authok"})
    else:
        return jsonify({"msg": "google failed"})

"""