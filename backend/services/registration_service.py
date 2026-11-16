from typing import List
from models import Registration
from database import registrations_db

def save_registration(reg: Registration):
    registrations_db[reg.id] = reg

def get_registration(reg_id: str) -> Registration:
    return registrations_db.get(reg_id)

def get_all_registrations() -> List[Registration]:
    return list(registrations_db.values())
