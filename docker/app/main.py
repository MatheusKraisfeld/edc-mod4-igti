from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def root():
    return {"message": "Teste FastAPI"}

@app.get("/api/{name}")
async def get_user(name):
    return {
        "name": name,
        "message": f"Hello, {name} from FastAPI."
    }