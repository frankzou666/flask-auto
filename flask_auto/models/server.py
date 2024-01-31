
from flask_auto import  db
class Server(db.Model):
    __tablename__="t_server"
    id = db.Column(db.Integer, primary_key=True)
    ip =  db.Column(db.String(200))
    status =  db.Column(db.Integer)

    def to_json(self):
        return {
            "id":self.id,
            "ip":self.ip,
            "status":self.status
        }