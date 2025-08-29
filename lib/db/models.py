from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class UserProgress(Base):
    __tablename__ = 'user_progress'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))
    status = Column(String)

    user = relationship("User", back_populates="progress")
    skill = relationship("Skill", back_populates="progress")


class follows(Base):
    __tablename__ = 'follows'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('users.id'))
    followed_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=func.now())

    follower = relationship("User", foreign_keys=[follower_id], back_populates="following")
    followed = relationship("User", foreign_keys=[followed_id], back_populates="followers")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    role = Column(String)
    created_at = Column(DateTime, default=func.now())

    skills = relationship("Skill", back_populates="creator", cascade="all, delete-orphan")
    progress = relationship("UserProgress", back_populates="user", cascade="all, delete-orphan")
    followers = relationship(
        "follows",
        foreign_keys="[follows.followed_id]",
        back_populates="followed",
        cascade="all, delete-orphan"
    )
    following = relationship(
        "follows",
        foreign_keys="[follows.follower_id]",
        back_populates="follower",
        cascade="all, delete-orphan"
    )


class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    description = Column(String)
    category = Column(String)
    created_by = Column(Integer, ForeignKey('users.id'))
    difficulty = Column(String)
    created_at = Column(DateTime, default=func.now())

    creator = relationship("User", back_populates="skills")
    progress = relationship("UserProgress", back_populates="skill", cascade="all, delete-orphan")


# --- Database setup ---
DATABASE_URL = "sqlite:///micro.db"
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)