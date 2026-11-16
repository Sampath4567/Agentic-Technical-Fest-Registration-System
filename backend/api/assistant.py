from fastapi import APIRouter, HTTPException
from schemas import AskRequest, AskResponse
from rag.query_agent import ask_question

router = APIRouter()

@router.post("/ask_event", response_model=AskResponse)
def ask_event(req: AskRequest):
    try:
        answer, sources = ask_question(req.question)
        return AskResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
