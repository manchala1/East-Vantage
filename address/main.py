from typing import Optional

from fastapi import FastAPI , Depends , Response
from . import schemas , db , models
from .db import engine
from sqlalchemy.orm import Session 

app = FastAPI()

get_db = db.get_db
models.Base.metadata.create_all(engine)

@app.get("/addresses/") # Get the Address In the Address Book
def get_all(db : Session = Depends(get_db)):
    address = db.query(models.Address).all()
    return address

@app.post('/createaddress/',response_model=schemas.Address) # Post the Address In to the Address Book
def create_address(request: schemas.Address,db : Session = Depends(get_db)):
    new_address = models.Address(**request.dict())
    print(new_address)
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address

@app.delete('/addresses/{id}') # Delete the Address In the Address Book Using database id
def delete_address(id: int,db : Session = Depends(get_db)):
    address = db.query(models.Address).filter(models.Address.id == id).first()
    db.delete(address)
    db.commit()
    return {"Address Deleted from The DataBase"}

@app.put('/addresses/{id}', response_model=schemas.Address) # Update the Address In the Address Book Using Database Id
def update_address(id: int, request: schemas.Address,db : Session = Depends(get_db)):
    address = db.query(models.Address).filter(models.Address.id == id).first()
    address.street = request.street
    address.city = request.city
    address.state = request.state
    address.zip = request.zip
    address.lat = request.lat
    address.lng = request.lng
    db.commit()
    return address

# retrieve all the addresses that are between the coordinates 
@app.get('/addresses/{lat}/{lng}')
def get_address_by_coordinates(lat: float, lng: float,db : Session = Depends(get_db)):
    address = db.query(models.Address).filter(models.Address.lat <= lat, models.Address.lng <= lng).all()
    return address