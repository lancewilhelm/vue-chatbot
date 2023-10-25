from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os
import openai
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

# read local .env file
_ = load_dotenv(find_dotenv())

# Connect to MongoDB
uri = os.environ["MONGO_URI"]
client = MongoClient(uri)
db = client['vue-chatbot']
messages_collection = db['messages']
messages_collection.delete_many({}) # Clear the messages collection
messages_collection.insert_one({'role': 'system', 'content': 'You are a helpful assistant'}) # Add a system message

# Get the API key from environment variables
openai.api_key = os.environ["OPENAI_API_KEY"]

# Create a OpenAI ChatGPT completion function
def get_chat_response():
    messages = get_messages()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    messages_collection.insert_one({'role': 'assistant', 'content': response.choices[0].message['content']})

def get_messages():
    messages = list(messages_collection.find({}))
    for message in messages:
        message.pop('_id')
    return messages

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
            if message_data['type'] == 'get_messages':
                messages = get_messages()
                await websocket.send_text(json.dumps({'type': 'message_update', 'content': messages[1:]}))

            if message_data['type'] == 'new_message':
                new_message = message_data['content']
                messages_collection.insert_one({'role': 'user', 'content': new_message})
                messages = get_messages()
                await websocket.send_text(json.dumps({'type': 'message_update', 'content': messages[1:]}))
                get_chat_response()
                messages = get_messages()
                await websocket.send_text(json.dumps({'type': 'message_update', 'content': messages[1:]}))

            if message_data['type'] == 'clear_messages':
                messages_collection.delete_many({})
                messages_collection.insert_one({'role': 'system', 'content': 'You are a helpful assistant'})
                messages = get_messages()
                await websocket.send_text(json.dumps({'type': 'message_update', 'content': messages[1:]}))

    except WebSocketDisconnect:
        print("Client disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)