from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from groq_client.client import generate_text

router = APIRouter()

class PromptIn(BaseModel):
    prompt: str

@router.post("/generate")
async def generate(body: PromptIn):
    """
    Accepts JSON: {"prompt": "<your text>"} and returns {"response": "<model text>"}.
    """
    try:
        text = generate_text(body.prompt)
        return {"response": text}
    except Exception as e:
        # keep it simple for now; in production prefer not to leak internal errors
        raise HTTPException(status_code=500, detail=str(e))
