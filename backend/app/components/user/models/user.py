from sqlalchemy import String, Uuid, Column, text
from sqlalchemy.orm import relationship
from ....db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Uuid(), server_default=text("gen_random_uuid()"), primary_key=True)
    email = Column(String(), nullable=False, unique=True)
    name = Column(String(), nullable=False, unique=False)
    password = Column(String(), nullable=False)
    images = relationship("Image", back_populates="user")
    tasks = relationship("Task", back_populates="user")
