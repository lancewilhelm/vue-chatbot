# vue-chatbot

A simple LLM-powered chatbot webapp in Vue.js with FastAPI backend

## Running the app

The easiest way to run this app and part of the intention of its creation is to run it via the `docker-compose` functionality. This will start the backend which hosts the page, the database and run them in containers. The only thing you need to do is to create a `.env` file in the root directory of the project and add your OpenAI API key there. The file should look like this:

```bash
OPENAI_API_KEY=your_api_key
```

Then you can run the app with `docker-compose up --build`. This will build the containers and start them. The app will be available at `localhost:8000`.

## Steps to reproduce

1. Create a new Vue.js project with `npm create vue@latest`. This will require Node.js and npm to be installed.
2. Follow the steps to get your first page up and running, `cd app`, `npm install`, `npm run dev`.
3. Observe the structure of the project and the files created. Two screenshots here, one of page and one of file structure.
4. Get rid of the current contents as we are going to put in our own. Chat content, and input bar
5. Style the components and make them look like they should by adding things in them.
6. Create the backend with FastAPI. `pip install fastapi` and `pip install uvicorn`. Python <= 3.11 is required. Create a new file called `main.py`. We are also going to use OpenAI API so `pip install openai` and `pip install python-dotenv`.
7. Build the page with `npm run build` and then update the backend to host the static page.
8. Let's make them talk with a websocket. `npm install reconnecting-websocket`, `pip install websockets`.
9. Incorporate OpenAI API key and make the backend talk to OpenAI API. Use `.env` file to store the API key.
10. Create a mongodb backend to store all the data
11. Dockerize

## Installation
