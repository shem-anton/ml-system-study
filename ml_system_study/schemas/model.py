from pydantic import BaseModel
from typing import List


class Model(BaseModel):
    name: str
    parameters: List[float]