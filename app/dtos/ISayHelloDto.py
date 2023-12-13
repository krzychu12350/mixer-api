from fastapi import UploadFile, File
from pydantic import BaseModel

class ISayHelloDto(BaseModel):
    file: UploadFile