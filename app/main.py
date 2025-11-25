from fastapi import FastAPI
from app.routers import user_router
from app.core.database import engine, Base


app = FastAPI(title='job search API')
Base.metadata.create_all(bind=engine)
app.include_router(user_router.router)
