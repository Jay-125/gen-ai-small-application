from typing import Union
from pydantic import BaseModel

class Base(BaseModel):
    email_id : Union[str, None]
    
class description(Base):
    description: str
