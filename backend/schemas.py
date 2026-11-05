from typing import List, Optional
from pydantic import BaseModel
from models import Member

class RegisterRequest(BaseModel):
    event_id: str
    team_name: str
    members: List[Member]
    payment_confirmed: bool

class RegisterResponse(BaseModel):
    registration_id: str
    eligibility_status: str
    slot_status: str
    waitlist_position: Optional[int] = None
    payment_verified: bool
    messages: List[dict]

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str
    sources: List[dict]
