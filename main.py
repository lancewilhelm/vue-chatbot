from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Set static file location
app.mount("/assets", StaticFiles(directory="app/dist/assets", html=True), name="static")

# Setup Jinja2 templates to serve index.html
templates = Jinja2Templates(directory="app/dist")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)