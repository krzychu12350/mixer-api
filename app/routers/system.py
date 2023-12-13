from fastapi import APIRouter, UploadFile

from app import __version__

router = APIRouter(tags=["System"])


@router.get("/status")
def status():
    return {"ok": True, "version": __version__}

@router.post("/multi")
async def mix_files(instrumental: UploadFile):
    # filePath = mixFileSounds(files, instrumental)
    #
    # return FileResponse(filePath, media_type='audio/wav')
    return {"instrumental": instrumental.filename}