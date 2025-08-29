from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, User, Skill, follows

DATABASE_URL = "sqlite:///micro.db"   

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

def seed_data():

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()

    try:
        # Seed Users
        user1 = User(username="alice", role="learner")
        user2 = User(username="bob", role="mentor")
        session.add_all([user1, user2])
        session.commit()  
        # Seed Skills 
        skill1 = Skill(
            title="Python Basics",
            description="Learn variables, loops, and functions.",
            category="Programming",
            created_by=user2.id,   
            difficulty="Beginner"
        )
        skill2 = Skill(
            title="SQL Fundamentals",
            description="Understand tables, queries, and joins.",
            category="Databases",
            created_by=user2.id,
            difficulty="Beginner"
        )
        skill3 = Skill(
            title="Git & GitHub",
            description="Version control basics with Git.",
            category="Tools",
            created_by=user2.id,
            difficulty="Beginner"
        )
        skill4 = Skill(
            title="Data Analysis",
            description="Intro to pandas, NumPy, and visualization.",
            category="Data Science",
            created_by=user2.id,
            difficulty="Intermediate"
        )
        skill5 = Skill(
            title="APIs",
            description="Learn how to interact with REST APIs in Python.",
            category="Backend",
            created_by=user2.id,
            difficulty="Intermediate"
        )

        session.add_all([skill1, skill2, skill3, skill4, skill5])
        # Seed Follows
        follow = follows(follower_id=user1.id, followed_id=user2.id)
        session.add(follow)
        session.commit()

		

        
        session.commit()
        print("✅ Database seeded successfully!")

    except Exception as e:
        session.rollback()
        print(f"Error seeding database: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    seed_data()
