from fastapi import FastAPI, __version__

from .routers import system

app = FastAPI()
app.include_router(system.router, prefix="/system")

@app.get("/statuss")
def status():
    return {"ok": True, "version": __version__}
