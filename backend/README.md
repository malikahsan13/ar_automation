FastAPI + Auth + DB Core

pip install fastapi uvicorn python-dotenv
pip install sqlalchemy alembic
pip install pymysql  # MySQL driver
pip install passlib[bcrypt]  # Password hashing
pip install python-jose[cryptography]  # JWT tokens
pip install pydantic


Background Jobs / Cron Jobs
Option 1: With APScheduler (for simple cron jobs)

pip install apscheduler

Option 2: With Celery (for distributed queue and cron jobs)

pip install celery redis

Excel Uploads / Parsing

pip install pandas openpyxl

Development / Debugging (optional but helpful)

pip install httpx
pip install ipython

CORS (Frontend-Backend Communication)

pip install fastapi[all]

