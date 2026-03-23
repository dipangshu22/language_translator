from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
translator = Translator()

# Allow mobile / web apps to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

languages = {
    "hindi": "hi",
    "french": "fr",
    "chinese": "zh-CN",
    "bengali": "bn",
    "punjabi": "pa",
    "persian": "fa",
    "spanish": "es",
    "nepali": "ne",
    "vietnamese": "vi",
    "russian": "ru",
    "malayalam": "ml",
    "telugu": "te",
    "thai": "th",
    "japanese": "ja",
    "korean": "ko",
    "assamese": "as"
}

class TranslateRequest(BaseModel):
    text: str
    language: str


@app.get("/")
def home():
    return {"message": "Translator API running"}




@app.post("/translate")
def translate(req: TranslateRequest):
    lang = req.language.lower()

    if lang not in languages:
        return {"error": "Language not supported"}

    try:
        result = translator.translate(req.text, dest=languages[lang])
        return {"translated": result.text}

    except Exception as e:
        return {"error": str(e)}
    
    
    