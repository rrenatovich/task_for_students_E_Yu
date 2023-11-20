from dataclasses import dataclass 

@dataclass 
class CustomerTravelEleven:
    id: int 
    numberPerson: int 
    direction: str
    sex: str 
    StartDate: str
    EndDate: str
    totalBill: str
    consultation: bool
    websitePage: str 
    consultationDuration: float #секунды

@dataclass 
class CustomerMed: 
    id: int 
    numberPerson: int 
    direction: str
    sex: str 
    date: str
    totalBill: str
    consultation: bool
    websitePage: str 
    consultationDuration: float #секунды


