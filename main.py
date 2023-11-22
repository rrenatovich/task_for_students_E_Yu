from src.model import ModelTravel
from src.customers_dataclasses import CustomerTravelEleven

if __name__ == '__main__': 
    model = ModelTravel(1/10800,1/9000,3, 'Travel')

    model.cycle()

    model1 = ModelTravel(1/10000,1/200, 200, 'Med')
    model1.cycle()