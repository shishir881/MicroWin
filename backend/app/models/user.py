# app/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    # --- The Neuro-Profile (Stored Encrypted) ---
    # Example: "I need extra steps for cleaning", "Dense text is hard"
    encrypted_preferences = Column(String, nullable=True) 
    
    # Example: "Kitchen", "Socializing", "Work"
    encrypted_struggle_areas = Column(String, nullable=True)
    
    # Scale of 1-5 (How small should the steps be?)
    granularity_level = Column(Integer, default=3) 

    tasks = relationship("Task", back_populates="owner")