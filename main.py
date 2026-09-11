from fastapi import FastAPI

app = FastAPI()

@app.get('/healthz')
def healthcheck():
    return {"status":"ok"}

@app.get("/")
def read_root():
    return {"message":"AI z aplikacji kontenerowej"}