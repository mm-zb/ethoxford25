from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routes import conversion, transaction, ai, health

app = FastAPI()

# Mount static files (CSS, JS, Images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 Templates
templates = Jinja2Templates(directory="templates")

# Include API routers
app.include_router(conversion.router)
app.include_router(transaction.router)
app.include_router(ai.router)
app.include_router(health.router)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "ts pmo"})
