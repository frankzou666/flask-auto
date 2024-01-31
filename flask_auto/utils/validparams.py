
from flask import  jsonify

from flask_auto import db
from flask_auto.models.user import User
from flask_auto.utils.tokenrequired import token_required
from flask_auto.utils.verccode import VercCode
from flask_auto.utils.apicode import ApiCode

def validParams(valid_params=None,request_params=None):
    if valid_params.sort()!=[item for item in request_params.keys()].sort():
        return ApiCode.paramsIncomplete()
    for key in request_params.keys():
        if len(request_params.get(key))==0:
            return ApiCode.paramsValueNull()



