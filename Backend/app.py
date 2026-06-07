from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from pipeline.outreach import (
    preview_pipeline,
    send_emails
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # temporary
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PreviewRequest(BaseModel):
    domain: str


class SendRequest(BaseModel):
    contacts: list


@app.get("/")
def root():
    return {"status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/preview")
def preview(request: PreviewRequest):
    return preview_pipeline(request.domain)


@app.post("/send")
def send(request: SendRequest):

    result = send_emails(request.contacts)

    return {
        "success": True,
        "result": result
    }