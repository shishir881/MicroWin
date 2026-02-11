from sqlalchemy import Column, Integer, Boolean, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    # Encrypted goal
    encrypted_goal = Column(LargeBinary, nullable=False)
    is_completed = Column(Boolean, default=False)
    
    # Relationship: Connects to MicroWinModel
    # cascade="all, delete-orphan" means if you delete a Task, its steps are also deleted.
    micro_wins = relationship("MicroWinModel", back_populates="owner", cascade="all, delete-orphan")

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
    owner = relationship("Task", back_populates="micro_wins")