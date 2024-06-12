from database import db
import jwt
from datetime import datetime
class user(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    def __init__(self, name, email, password, phone, role):
        self.name=name
        self.email=email
        self.password=password
        self.phone=phone
        self.role=role
    def save(self):
        db.session.add(self)
        db.commit()
    def get_all():
        return user.query.all()
    def get_by_id(id):
        return user.query.get(id)
    def update(self, name=None, email=None, password=None, phone=None, role=None):
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if role is not None:
            self.role = role
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                'SECRET_KEY',
                algorithm='HS256'
            )
        except Exception as e:
            return e
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, 'SECRET_KEY')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
        except Exception as e:
            return e