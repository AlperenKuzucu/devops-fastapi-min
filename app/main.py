from typing import Any
from fastapi import FastAPI, Body, Depends

from .config import Settings, get_settings
from .version import __version__

app = FastAPI(title="DevOps FastAPI Minimal")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/version")
def version(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    return {
        "version": __version__,
        "commit": settings.commit,
        "env": settings.env,
    }

@app.post("/echo")
def echo(payload: Any = Body(...)) -> Any:
    # Gelen JSON'u aynen geri döndürür
    return payload
