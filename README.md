# phase-3-project

My CLI application project

# 🎓 Micro Skills CLI

This is an interactive CLI application written using python and uses SQL for its database

# How to create a new user(learner or mentor)

Inside the PHASE-3-PROJECT directory you: 

Run "python -m lib.cli create-user <username> <role>" while inside the directory using your operating system's own cli

# How to get your user account

Run "python -m lib.cli get-user <username>" while inside the directory using your operating system's own cli.

# How to update the user role 

Run "python -m lib.cli update-user <username> <ner_role>" while inside the directory using your operating system's own cli.

# How to delete user

Run "python -m lib.cli delete-user <username>" while inside the directory using your operating system's own cli.

# How to select a skill

Run "python -m lib.cli select-skill <skill_name>" while inside the directory using your operating system's own cli.

#  How to recomend a skill

Run "python -m lib.cli recommend-skill" while inside the directory using your operating system's own cli.

# How to follow 

Run "python -m lib.cli follow <username>" while inside the directory using your operating system's own cli.

# Colors and Output

✅Green - Success
❌Red - Errors
🔄Yellow - Updates
👤Cyan - User info
🗑️Magenta - Deletes

# Project Structure

phase-3-project/
│── .venv/
│── lib/
|   ├── __pycache__/
|   ├── __init__.py
|   ├── debug.py
|   ├── micro.db
│   ├── cli.py          
│   ├── helpers.py      
│   └── db/
|       ├── __pycache__/
|       ├── migrations/
|       ├── __init__.py
│       ├── models.py   
│       ├── seed.py     
│       └── micro.db    
│── LICENSE
│── micro.db
│── Pipfile
│── Pipfile.lock
│── requirements.txt
│── README.md

