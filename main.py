from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,func,create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
Base = declarative_base()

class Users(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String, unique=True)
	role = Column(String)
	created_at = Column(DateTime, default=func.now())
class skills(Base):
	__tablename__ = 'skills'
	id = Column(Integer, primary_key=True)
	title = Column(String, unique=True)
	description = Column(String)
	category = Column(String)
	created_by = Column(Integer, ForeignKey('users.id'))
	difficulty = Column(String)
	created_at = Column(DateTime, default=func.now())


class User_progress(Base):
	__tablename__ = 'user_progress'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	skill_id = Column(Integer, ForeignKey('skills.id'))
	status = Column(String)

class follows(Base):
	__tablename__ = 'follows'
	id = Column(Integer, primary_key=True)
	follower_id = Column(Integer, ForeignKey('users.id'))
	followed_id = Column(Integer, ForeignKey('users.id'))
	created_at = Column(DateTime, default=func.now())


DATABASE_URL = "sqlite:///micro.db"
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)