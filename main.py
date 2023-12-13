from time import time

import uvicorn
from fastapi import FastAPI, __version__, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from mixer import Mixer

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# def validateFiles(files):
#     for file in files:
#         # # Get the file size (in bytes)
#         # file.file.seek(0, 2)
#         # file_size = file.file.tell()
#         #
#         # # move the cursor back to the beginning
#         # await file.seek(0)
#         #
#         # if file_size > 2 * 1024 * 1024:
#         #     # more than 2 MB
#         #     raise HTTPException(status_code=400, detail="File too large")
#         #
#         # check the content type (MIME type)
#         content_type = file.content_type
#         if content_type not in ["audio/mp3", "audio/wav", "audio/x-wav"]:
#             raise HTTPException(status_code=400, detail="Invalid file type. Must be audio/mp3")


# @app.get("/mp3")
# async def root():
#     mixer = Mixer()
#     filePath = mixer.mergeFiles()
#     # return {"message": "Welcome test", "fileName": filePath}
#     return FileResponse(filePath, media_type='audio/mp3')


@app.post("/multi")
async def check_multi_files(files: list[UploadFile], instrumental: UploadFile):
    mixer = Mixer()
    filePath = mixer.mixFileSounds(files, instrumental)

    return FileResponse(filePath, media_type='audio/wav')
    # return {"filenames": [file.filename for file in files], "instrumental": instrumental.filename}


# @app.get("/mix")
# async def mix_files():
#     mixer = Mixer()
#     filePath = mixer.mixFileSounds()
#     return FileResponse(filePath, media_type='audio/mp3')


@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}


@app.get('/')
async def helloWorld():
    return {'res': 'HelloWorld'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
