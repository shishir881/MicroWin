from sqlalchemy import Column, Integer, Boolean, LargeBinary, ForeignKey,String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True) # <--- For your Sidebar (e.g., "Singing Practice")
    encrypted_goal = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_completed = Column(Boolean, default=False)
    
    # User Relationship
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True) # Set nullable=False later after auth
    owner = relationship("User", back_populates="tasks")

    micro_wins = relationship("MicroWinModel", back_populates="parent_task", cascade="all, delete-orphan")

class MicroWinModel(Base):
    __tablename__ = "micro_wins"

    id = Column(Integer, primary_key=True, index=True)
    # The Foreign Key: This links every step to a specific Task ID
    task_id = Column(Integer, ForeignKey("tasks.id"))
    
    # Encrypted action (The "Micro-Win")
    encrypted_action = Column(LargeBinary, nullable=False)
    is_completed = Column(Boolean, default=False)
    step_order = Column(Integer) # To keep steps in 1, 2, 3 order

    # Back-reference to the parent Task
    parent_task = relationship("Task", back_populates="micro_wins")