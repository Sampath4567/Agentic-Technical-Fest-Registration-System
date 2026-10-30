# Simple in-memory storage for demonstration
from typing import Dict
from models import Registration

# In-memory store: registration_id -> Registration
registrations_db: Dict[str, Registration] = {}
