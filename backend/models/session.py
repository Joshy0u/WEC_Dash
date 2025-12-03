from pydantic import BaseModel, ConfigDict, Field, model_validator
import sys
import os
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fileParser import load_parsed_data

class SessionModel(BaseModel):
    fastest_lap_count: int = Field(gt=0)
    fastest_lap_time: float
    total_laps: int = Field(ge=1, le=100)
    
    @model_validator(mode="after")
    def check_fastest_lap_time(self):
        if self.fastest_lap_count > self.total_laps:
            raise ValueError("Fastest lap count cannot exceed total laps.")
        return self
    
data = load_parsed_data()
pprint(data)
#ok note i need to convert from MM:SS.mmm to float seconds
m = SessionModel(
    fastest_lap_count=5,
    fastest_lap_time= 83.456, 
    total_laps=10
)
pprint(m.model_dump())
# i need to test with the actual dictionary from the parser
