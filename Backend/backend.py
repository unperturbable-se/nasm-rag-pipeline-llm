from fastapi import FastAPI,Body
from fastapi.middleware.cors import CORSMiddleware
from rag_maker import  get_rag_response,select_client,start
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allows requests from your local HTML file
    allow_credentials=True,
    allow_methods=["*"],      # Explicitly allows OPTIONS, POST, GET, etc.
    allow_headers=["*"],      # Allows Content-Type and custom headers
)

@app.post("/query")
def q0(question:dict=Body(...)):
    answer=get_rag_response(question["Query"])
    return {"Query":question, "Answer":answer}

@app.post("/model_selection")
def select_model(choice:dict=Body(...)):
    select_client(choice["key"],choice["url"],choice["model"])

@app.get("/start")
def q1():
    start()
    

#api_key="gsk_abcdefg",
#base_url="https://api.groq.com/openai/v1",
#model="meta-llama/llama-prompt-guard-2-86m"