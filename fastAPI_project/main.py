import uvicorn as uvicorn
from fastapi import FastAPI
from fastAPI_project.api import group_api


app = FastAPI(
    docs_url='/api/docs'
)

app.include_router(group_api.router, prefix='/api/v1/group')

@app.get
async def root():
    return {"message": "Hello, world"}

@app.get
async def say_hello(name: str):
    return {"message": f"Hello, {name}"}

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8001
    )
