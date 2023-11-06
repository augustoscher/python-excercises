from fastapi import FastAPI

app = FastAPI()


@app.get("/health/liveness")
async def liveness():
    return {"status": "ok"}


@app.get("/health/readiness")
async def readiness():
    return {"status": "ok"}
