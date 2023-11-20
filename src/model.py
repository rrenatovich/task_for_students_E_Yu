import random 
from operator import attrgetter
from datetime import datetime
from .customers_dataclasses import CustomerTravelEleven
from .log_builder import fillOrderInfo, writeCSV
customerList = []

class InputFlow:
    def __init__(self, parameter):
        self.parameter = parameter
    def get_time(self):
        return random.expovariate(self.parameter)

class Customer():
    def __init__(self, startTime): 
        self.startTime = startTime
    
    def getEndTime(self, param):
        self.endTime = random.expovariate(param)

class Model: 
    def __init__(self, lmbd, mu, blockSize):
        self.inputFlow = InputFlow(lmbd)
        self.service_param = mu
        self.blockSize = blockSize
        
        self.doneCustomers : int = 0 

        self.customersList = []
        self.time = 1641018049 # старт 01 01 2022

    def oneItteration(self):
        if len(self.customersList) == 0: 
            time = self.inputFlow.get_time()
            self.time += time
            customer = Customer(self.time)
            customer.getEndTime(self.service_param)
            self.customersList.append(customer)
        else: 
            t1 = self.inputFlow.get_time()
            next_event = min(self.customersList, key=attrgetter('endTime'))
            if t1 < next_event.endTime: 
                self.time += t1
                if len(self.customersList) + 1 <= self.blockSize:
                    customer = Customer(self.time)
                    customer.getEndTime(self.service_param)
                    self.customersList.append(customer)
                else: 
                    pass 
            else: 
                self.time += next_event.endTime
                next_event.endTime = self.time
                # print(f' {datetime.fromtimestamp(next_event.startTime)}, {datetime.fromtimestamp(next_event.endTime)}')
                self.customersList.remove(next_event)
                customerList.append(fillOrderInfo(datetime.fromtimestamp(next_event.startTime), datetime.fromtimestamp(next_event.endTime) )) 

    
    def cycle(self): 
        counter = 0 
        while counter != 100000: 
            self.oneItteration()
            counter += 1
        print('done')
        writeCSV(customerList)
