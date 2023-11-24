from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"mensaje": "Bienvenidos a la api de productos"}  