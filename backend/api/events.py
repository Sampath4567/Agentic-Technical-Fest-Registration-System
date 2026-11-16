from fastapi import APIRouter, HTTPException
from typing import List
from models import Event
from services.event_service import get_all_events, get_event

router = APIRouter()

@router.get("/events", response_model=List[Event])
def list_events():
    return get_all_events()

@router.get("/events/{event_id}", response_model=Event)
def get_event_details(event_id: str):
    event = get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
