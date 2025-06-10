from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.pdf_reader import extract_text_from_pdf
from utils.ai_engine import analyze_lease
import shutil
import uuid
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    email: str
    report: dict

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        file_id = f"{uuid.uuid4()}.pdf"
        file_path = Path("uploads") / file_id
        Path("uploads").mkdir(parents=True, exist_ok=True)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        text = extract_text_from_pdf(file_path)
        result = analyze_lease(text)

        return JSONResponse(content=result)

    except Exception as e:
        print("❌ ERROR:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/email")
async def email_summary(req: EmailRequest):
    print(f"📧 Sending summary to: {req.email}")
    print("Report preview:", req.report)
    return {"message": f"Summary sent to {req.email} (simulated)"}