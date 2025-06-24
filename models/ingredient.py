from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    brand_name = Column(String, nullable=True)
    serving_size = Column(String, nullable=True)
    quantity = Column(Integer, default=1)
    calories = Column(Integer, default=0)
    protein = Column(Integer, default=0)
    carbohydrates = Column(Integer, default=0)
    date_created = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Ingredient %r>' % self.id