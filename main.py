
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from utils.pdf_reader import extract_text_from_pdf
from utils.ai_engine import analyze_lease
import shutil
import uuid
from pathlib import Path

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    file_id = f"{uuid.uuid4()}.pdf"
    file_path = Path("uploads") / file_id

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)
    result = analyze_lease(text)

    return JSONResponse(content=result)
