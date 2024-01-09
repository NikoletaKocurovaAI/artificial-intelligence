from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Robot(Base):
    __tablename__ = "robot"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    motor_type = Column(Text)
