
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils.pdf_reader import extract_text_from_pdf
from utils.ai_engine import analyze_lease
import shutil
import uuid
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can later restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        file_id = f"{uuid.uuid4()}.pdf"
        file_path = Path("uploads") / file_id

        # 🔥 This line ensures the uploads/ folder exists
        Path("uploads").mkdir(parents=True, exist_ok=True)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("✅ Saved file:", file_path)

        text = extract_text_from_pdf(file_path)
        print("📄 Extracted text length:", len(text))

        result = analyze_lease(text)
        print("🤖 AI result:", result)

        return JSONResponse(content=result)

    except Exception as e:
        print("❌ ERROR:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})
