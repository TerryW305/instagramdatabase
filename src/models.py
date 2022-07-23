import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base)
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String, nullable=False)
    firs_tname = Column(String(30), unique=True, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String(16), unique=True, nullable=False)

class Followers(Base):
    __tablename__ = 'followers' 
    user = relationship('User')
    use_from_id = Column(Integer, ForeignKey('User_id), nullable=True)
    use_to_id = Column(Integer, ForeignKey('User_id), nullable=True)


render_er(Base, 'diagram.png')
