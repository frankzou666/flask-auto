

class ApiCode():
    def __init__(self):
        pass

    @staticmethod
    def userNotExist(status='error',code='userNotExist',msg='用户不存在',data=[]):
        return  {'status':status,'code':code,'msg':msg,'data':data}

    @staticmethod
    def paramsIncomplete(status='error',code='paramsIncomplete',msg='参数不完整',data=[]):
        return {'status': status, 'code': code, 'msg': msg, 'data': data}

    @staticmethod
    def loginSuccess(status='ok', code='loginSuccess', msg='登录成功', data=[]):
        return {'status': status, 'code': code, 'msg': msg, 'data': data}

    @staticmethod
    def passwordIncorrect(status='error', code='passwordIncorrect', msg='密码错误', data=[]):
        return {'status': status, 'code': code, 'msg': msg, 'data': data}

    @staticmethod
    def logoutSuccess(status='ok', code='logoutSuccess', msg='退出登录', data=[]):
        return {'status': status, 'code': code, 'msg': msg, 'data': data}

    @staticmethod
    def logoutFailed(status='error', code='logoutFailed', msg='退出登录失败', data=[]):
        return {'status': status, 'code': code, 'msg': msg, 'data': data}

    @staticmethod
    def createUsersSuccess(status='ok', code='createUsersSuccess', msg='创建用户成功', data=[]):
        return {'status': status, 'code': code, 'msg': msg, 'data': data}

    @staticmethod
    def getVerifyCodeSuccess(status='ok', code='getVerifyCodeSuccess', msg='获取验证码成功', data=[]):
        return {'status': status, 'code': code, 'msg': msg, 'data': data}


    @staticmethod
    def paramsValueNull(status='error', code='paramsValueNull', msg='参数值为空', data=[]):
        return {'status': status, 'code': code, 'msg': msg, 'data': data}