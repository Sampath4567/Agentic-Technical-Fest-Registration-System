from typing import List, Optional
from pydantic import BaseModel, Field

class Event(BaseModel):
    id: str
    name: str
    description: str
    min_year: int
    max_year: int
    allowed_branches: List[str]
    min_team_size: int
    max_team_size: int
    max_teams: int
    fee: float
    date: str
    time: str
    venue: str
    rules: List[str]

class Member(BaseModel):
    name: str
    email: str
    phone: str
    year: int
    branch: str
    college: str

class Registration(BaseModel):
    id: str
    event_id: str
    team_name: str
    members: List[Member]

    payment_transaction_id: Optional[str] = None
    payment_amount: float = 0.0

    eligibility_status: str = "pending"
    eligibility_reasons: List[str] = Field(default_factory=list)

    slot_status: str = "pending"
    waitlist_position: Optional[int] = None

    payment_verified: bool = False
    payment_issues: List[str] = Field(default_factory=list)

    messages: List[dict] = Field(default_factory=list)
    risk_flags: List[str] = Field(default_factory=list)
    
    registration_date: str = ""
