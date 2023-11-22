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
    consultationDuration: float #минуты

@dataclass 
class CustomerMed: 
    id: int 
    category: str
    serviceCategory: str
    numberPerson: int 
    sex: str 
    vote: int
    StartDate: str
    EndDate: str
    


