# DealPrūf Backend – FastAPI

This is the backend service for DealPrūf, built with FastAPI and ready for deployment on [Render.com](https://render.com).

## 🚀 Features
- Upload and analyze lease PDFs
- Extract key lease terms
- Detect red flags
- Output structured JSON

## 📦 Folder Structure
```
dealpruf-backend/
├── main.py
├── utils/
│   ├── pdf_reader.py
│   └── ai_engine.py
├── models/
│   └── schemas.py
├── uploads/
├── requirements.txt
├── render.yaml
```

## 🛠 Deploy to Render

1. Push this folder to a GitHub repo
2. Go to https://render.com and create a free account
3. Click “New Web Service”
4. Connect your GitHub and select this repo
5. Render will auto-detect `render.yaml` and deploy

Access your live API at: `https://your-app-name.onrender.com/docs`