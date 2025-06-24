from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.base import Base

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    ingredient = relationship('Ingredient', remote_side=[id], backref='ingredients')

    def __repr__(self):
        return '<Recipe %r>' % self.id