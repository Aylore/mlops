from typing import Optional
from pydantic import BaseModel


class SamplePostRequest(BaseModel):
    a: int
    b: list
    c: Optional[str]






















