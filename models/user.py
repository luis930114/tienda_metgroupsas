from extensions import db
import hashlib

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def register(cls, username, password):
        hash_pwd = hashlib.sha256(password.encode()).hexdigest()
        user = cls(username=username, password_hash=hash_pwd)
        db.session.add(user)
        db.session.commit()
        return user

    def verify_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()