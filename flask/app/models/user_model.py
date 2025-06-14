from app.models import BaseModel
from app.db import db

class User(BaseModel):
    __tablename__ = 'user'
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = self.hash_password(password)
        
    def generate_token(self):
        token = Token(self.id, self.generate_hash())
        token.save()
        return token.token
        
    def generate_hash(self):
        import hashlib
        return hashlib.sha256(self.email.encode()).hexdigest()
    
    def hash_password(self, password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password):
        import hashlib
        pass_hash = hashlib.sha256(password.encode()).hexdigest()
        print(pass_hash)
        return pass_hash == self.password
    
    
        
        
        
class Token(BaseModel):
    __tablename__ = 'token'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(50), nullable=False)
    
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
