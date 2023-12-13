from sqlalchemy import ForeignKey, Uuid, Column, text, Enum, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from ..vo.status import Status
from ..vo.type import Type
from ....db.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Uuid(), server_default=text("gen_random_uuid()"), primary_key=True)
    user_id = Column(Uuid(), ForeignKey("users.id"), nullable=False)
    depends_on_id = Column(Uuid(), ForeignKey("tasks.id"), nullable=True)
    type = Column(Enum(Type, name='task_type'), nullable=False)
    data = Column(JSONB, nullable=True)
    result = Column(JSONB, nullable=True)
    status = Column(Enum(Status, name='task_status'), nullable=False)
    created_at = Column(DateTime, server_default=text("now()"), nullable=True)
    user = relationship("User", back_populates="tasks")
    depends_on = relationship("Task", remote_side=[id])


