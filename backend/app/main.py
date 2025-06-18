from fastapi import FastAPI
from app.api import auth
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router, prefix = "/auth", tags=["Auth"])