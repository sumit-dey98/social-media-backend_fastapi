from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# apis ================================
@app.get("/")
def root(  ):
    return {"message": "API Running on https://social-media-backend-fastapi.onrender.com/. Find the docs at https://social-media-backend-fastapi.onrender.com/docs/"}

# users api ================================
app.include_router(user.router)

# posts api ================================
app.include_router(post.router)

# auth api ================================
app.include_router(auth.router)

# votes api ================================
app.include_router(vote.router)
