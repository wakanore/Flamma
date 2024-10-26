from fastapi import FastAPI
from app.students.routers import router as router_users
from app.students.router import router as router_students
from starlette.requests import Request
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from app.students.excep import TokenNotFoundException


app = FastAPI(title="Flamma-Edu")




app.include_router(router_users)
app.include_router(router_students)




