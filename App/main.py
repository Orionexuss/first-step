from fastapi import FastAPI, Request
from . import models
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "https://www.google.com",
    "www.google.com/:1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#models.Base.metadata.create_all(bind=engine)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return{"message": "Hello World!!!"}

@app.middleware("http")
async def log_origin(request: Request, call_next):
    origin = request.headers.get("origin")
    print(f"Solicitud desde el origen: {origin}")
    response = await call_next(request)
    return response




