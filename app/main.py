from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from . import models
from .database import engine
from .routers import post,user,auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)

app=FastAPI()
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    message = "Welcome to my FastAPI project! Click <a href='https://fastapi-sudarshan.herokuapp.com/docs'>here</a> to access the API features through documentation."
    return HTMLResponse(content=message)