from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

messages = []

app = FastAPI()

# Set static file location
app.mount("/assets", StaticFiles(directory="app/dist/assets", html=True), name="static")

# Setup Jinja2 templates to serve index.html
templates = Jinja2Templates(directory="app/dist")

# Serve index.html template from the root path
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Create a websocket connection
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        message_data = json.loads(data)
        if message_data['type'] == 'get_messages':
            return_message = {'type': 'message_update', 'content': messages}
            await websocket.send_text(json.dumps(return_message))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)