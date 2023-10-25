# vue-chatbot

A simple LLM-powered chatbot webapp in Vue.js with FastAPI backend

## Steps to reproduce

1. Create a new Vue.js project with `npm create vue@latest`. This will require Node.js and npm to be installed.
2. Follow the steps to get your first page up and running, `cd app`, `npm install`, `npm run dev`.
3. Observe the structure of the project and the files created. Two screenshots here, one of page and one of file structure.
4. Get rid of the current contents as we are going to put in our own. Chat content, and input bar
5. Style the components and make them look like they should by adding things in them.
6. Create the backend with FastAPI. `pip install fastapi` and `pip install uvicorn`. Python <= 3.11 is required. Create a new file called `main.py`. We are also going to use OpenAI API so `pip install openai` and `pip install python-dotenv`.
7. Build the page with `npm run build` and then update the backend to host the static page.

## Installation
