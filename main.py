from src.model import Model, customerList
from src.customers_dataclasses import CustomerTravelEleven

if __name__ == '__main__': 
    model = Model(1/10800,1/7000,3)

    model.cycle()

