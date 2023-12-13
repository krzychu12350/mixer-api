from typing import Annotated

from fastapi import APIRouter, UploadFile, Form

from app import __version__

router = APIRouter(tags=["System"])


@router.get("/status")
def status():
    return {"ok": True, "version": __version__}

@router.post("/multi")
async def mix_files(instrumental):
    # filePath = mixFileSounds(files, instrumental)
    #
    # return FileResponse(filePath, media_type='audio/wav')
    return {"instrumental": instrumental.filename}

class Color(BaseModel):
    r: float
    g: float
    b: float

@app.post("/")
def api_test(color: Color = Form(...)):
    print(color)
    print(type(color))