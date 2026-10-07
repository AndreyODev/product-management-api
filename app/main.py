from fastapi import FastAPI
from routes.product_router import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"Message": "Product management API with FastAPI + MongoDB"}
