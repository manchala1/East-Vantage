from pydantic import BaseModel ,ValidationError , validator
from .db import Base

class Address(BaseModel): # Show Address class Schema
    street: str
    city: str
    state: str
    zip: str
    lat: float
    lng: float

    @validator('street')
    def street_beempty(cls,v):
        if not v:
            raise ValueError("Street Name must not be Empty")
        return v
    @validator('city')
    def city_beempty(cls,v):
        if not v:
            raise ValueError("City Name must not be Empty")
        return v
    @validator('state')
    def state_beempty(cls,v):
        if not v:
            raise ValueError("State Name must not be Empty")
        return v
    @validator('zip')
    def zip_beempty(cls,v):
        if not v:
            raise ValueError("zip Name must not be Empty")
        return v
    @validator('lat')
    def Lat(cls, v):
        print(v)
        if v < -90 or v>90:
            raise ValueError("Latitude should be in range -90 to 90")
        return v
    @validator('lng')
    def Lng(cls, v):
        print(v)
        if v < -180 or v>180:
            raise ValueError("Latitude should be in range -180 to 180")
        return v

    class Config():
        orm_mode = True

 
class ShowAddress(BaseModel):# Show Coordinates class Schema
    lat: float
    lng: float

    class Config():
        orm_mode = True