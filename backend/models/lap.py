from pydantic import BaseModel, Field, model_validator
import sys
import os
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fileParser import load_parsed_data

# need lap name and lap time
class LapModel(BaseModel):
    lap_name: str
    lap_time: float

    @model_validator(mode="after")
    def check_lap_time(self):
        if self.lap_time <= 0:
            raise ValueError("Lap time must be a positive value.")
        return self
    
data = load_parsed_data()

n = LapModel(
    lap_name=data['lap_data'][0]['lap_name'],
    lap_time=data['lap_data'][0]['lap_time']
)
pprint(n.model_dump())