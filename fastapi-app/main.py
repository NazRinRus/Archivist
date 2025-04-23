from fastapi import FastAPI
import uvicorn
from modules.file_search import get_files, get_file_content, get_json_from_list
import os

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)