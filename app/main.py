from fastapi import FastAPI
from crew_runner import run_crew

app = FastAPI()

@app.post("/evaluate")
def evaluate(payload: dict):
    idea = payload["idea"]
    result = run_crew(idea)
    return {"status": "done", "data": result}
