from fastapi import FastAPI
from app.students.routers import router as router_users
from starlette.requests import Request
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from app.students.excep import TokenNotFoundException


app = FastAPI(title="Flamma-Edu")




@app.get("/")
def home_page():
    return {"message": "Hello World"}

app.include_router(router_users)




