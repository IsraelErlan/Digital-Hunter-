from pydantic import BaseModel, ValidationError
from datetime import datetime, timezone
# from ...shared.logger import log_event


class Intel(BaseModel):
    timestamp: datetime 
    signal_id: str 
    entity_id: str
    reported_lat: float
    reported_lon: float
    signal_type: str
    priority_level: int


#add note
def validate_error(msg_intel: dict)-> None | str:
    try: 
        Intel(**msg_intel)
        return None
    except ValidationError as e: 
        # log_event(level="error", message=str(e))
        return str(e)



# a = {
#         "timestamp": datetime.now(timezone.utc).isoformat(),
#         "signal_id": "yy",
#         "entity_id": "o",
#         "reported_lat": 6.9,
#         "reported_lon": 9.8,
#         "signal_type": "uu",
#     }

# b = Intel(**a)
# print(b)