from fastapi import FastAPI
from models import engine, Base, SessionLocal
from route import router

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(router)
