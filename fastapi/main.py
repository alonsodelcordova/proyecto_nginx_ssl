from fastapi import FastAPI
app = FastAPI(root_path="/fastapi")

@app.get("/")
def read_root():
    return {"mensaje": "Hola desde FastAPI"}
