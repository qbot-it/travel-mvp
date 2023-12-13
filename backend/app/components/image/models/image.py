from sqlalchemy import ForeignKey, Uuid, Column, text, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from ....db.database import Base


class Image(Base):
    __tablename__ = "images"
    id = Column(Uuid(), server_default=text("gen_random_uuid()"), primary_key=True)
    user_id = Column(Uuid(), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="images")
    descriptor = Column(JSONB())
    hash = Column(String(), nullable=False)

