from fastapi import APIRouter, HTTPException, Depends
from typing import List
import uuid
from datetime import datetime

from schemas import RegisterRequest, RegisterResponse
from models import Registration
from services.event_service import get_event
from services.registration_service import save_registration, get_registration, get_all_registrations
from workflow.graph import registration_workflow
from utils.rbac import verify_participant, verify_admin

router = APIRouter()

@router.post("/register", response_model=RegisterResponse)
def register(req: RegisterRequest):
    event = get_event(req.event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
        
    registration_id = f"REG-{uuid.uuid4().hex[:8].upper()}"
    
    initial_state = {
        "registration_id": registration_id,
        "event": event,
        "team_name": req.team_name,
        "members": req.members,
        "eligibility_status": "pending",
        "eligibility_reasons": [],
        "slot_status": "pending",
        "waitlist_position": None,
        "payment_confirmed": req.payment_confirmed,
        "payment_transaction_id": None,
        "payment_amount": 0.0,
        "payment_verified": False,
        "payment_issues": [],
        "messages": []
    }
    
    final_state = registration_workflow.invoke(initial_state)
    
    reg_record = Registration(
        id=final_state['registration_id'],
        event_id=event.id,
        team_name=final_state['team_name'],
        members=final_state['members'],
        payment_transaction_id=final_state.get('payment_transaction_id'),
        payment_amount=final_state.get('payment_amount', 0.0),
        eligibility_status=final_state['eligibility_status'],
        eligibility_reasons=final_state['eligibility_reasons'],
        slot_status=final_state['slot_status'],
        waitlist_position=final_state['waitlist_position'],
        payment_verified=final_state['payment_verified'],
        payment_issues=final_state['payment_issues'],
        messages=final_state['messages'],
        registration_date=datetime.now().isoformat()
    )
    
    save_registration(reg_record)
    
    return RegisterResponse(
        registration_id=reg_record.id,
        eligibility_status=reg_record.eligibility_status,
        slot_status=reg_record.slot_status,
        waitlist_position=reg_record.waitlist_position,
        payment_verified=reg_record.payment_verified,
        messages=reg_record.messages
    )

@router.get("/registration/{registration_id}", response_model=Registration)
def get_registration_route(registration_id: str):
    reg = get_registration(registration_id)
    if not reg:
        raise HTTPException(status_code=404, detail="Registration not found")
    return reg

@router.get("/registrations", response_model=List[Registration])
def list_registrations(role: str = Depends(verify_admin)):
    return get_all_registrations()
