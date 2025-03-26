import uuid
from datetime import datetime

def generate_order_id():
    return f"O{datetime.utcnow().year}{uuid.uuid4().hex[:5]}"