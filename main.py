from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os
import openai
from dotenv import load_dotenv, find_dotenv

messages = [{'role': 'system', 'content': 'You are a helpful assistant'}]

# Get the API key from environment variables
_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]

# Create a OpenAI ChatGPT completion function
def get_chat_response():
    global messages
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    messages.append({'role': 'assistant', 'content': response.choices[0].message['content']})

app = FastAPI(debug=True)

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
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            print(message_data)
            if message_data['type'] == 'get_messages':
                return_message = {'type': 'message_update', 'content': messages[1:]}
                print(return_message)
                await websocket.send_text(json.dumps(return_message))

            if message_data['type'] == 'new_message':
                new_message = message_data['content']
                messages.append({'role': 'user', 'content': new_message})
                get_chat_response()
                return_message = {'type': 'message_update', 'content': messages[1:]}
                print(return_message)
                await websocket.send_text(json.dumps(return_message))

            if message_data['type'] == 'clear_messages':
                messages.clear()
                messages.append({'role': 'system', 'content': 'You are a helpful assistant'})
                return_message = {'type': 'message_update', 'content': messages[1:]}
                print(return_message)
                await websocket.send_text(json.dumps(return_message))

    except WebSocketDisconnect:
        print("Client disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)