from app.db import db


class BaseModel(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in self.__table__.columns}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()
        
    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"
    
    def __str__(self):  
        return f"<{self.__class__.__name__} {self.id}>"
    