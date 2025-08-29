import random
from lib.db.models import Skill

def get_skill_by_name(session, title: str):
    return session.query(Skill).filter_by(title=title).first()

def recommend_next_skill(session, exclude_id=None):
    query = session.query(Skill)
    if exclude_id:
        query = query.filter(Skill.id != exclude_id)
    all_skills = query.all()
    if not all_skills:
        return None
    return random.choice(all_skills)