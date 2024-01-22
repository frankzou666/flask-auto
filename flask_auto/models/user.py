from flask_auto import  db
import bcrypt
from flask import  current_app
from jwt import encode,decode
import  datetime



class User(db.Model):
    __tablename__="t_user"
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(200))
    password =  db.Column(db.String(200))

    def __init__(self,username=None,password=None):
        self.username=username
        self.password=bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def to_json(self):
        return  {"username":self.username,"password":self.password}

    def check_user_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8') ,hashed_password=self.password.encode("utf-8"))

    def encode_user_token(self):
        payload = {
            "exp":datetime.datetime.now() +datetime.timedelta(seconds=1800),
            "iat":datetime.datetime.utcnow(),
            "sub":self.id

        }
        token =encode(payload=payload,key=current_app.config.get("SECRET_KEY"),algorithm="HS256")
        return token

    @staticmethod
    def decode_user_token(jwt):
        payload =decode(jwt=jwt, key=current_app.config.get("SECRET_KEY"),algorithms=("HS256"))
        return payload





