from fastapi import FastAPI, HTTPException, Path, Query
from model.model import User
from serializer.serializer import convertdata, convertdatas
from routes.routes import endpoints

app = FastAPI()

app.include_router(endpoints)

