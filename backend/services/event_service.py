from typing import List
from models import Event
from data import events_db

def get_all_events() -> List[Event]:
    return list(events_db.values())

def get_event(event_id: str) -> Event:
    return events_db.get(event_id)
