import random 
from operator import attrgetter
from datetime import datetime
from .customers_dataclasses import CustomerTravelEleven
from .log_builder import fillOrderInfo, writeCSV


class InputFlow:
    def __init__(self, parameter):
        self.parameter = parameter
    def get_time(self):
        return random.expovariate(self.parameter)

class Customer():
    def __init__(self, startTime): 
        self.startTime = startTime
        self.value = 1
    
    def getEndTime(self, param):
        self.endTime = random.expovariate(param / self.value)

class ModelTravel: 
    def __init__(self, lmbd, mu, blockSize, flag):
        self.flag = flag
        self.time = 1641018049 # старт 01 01 2022
        self.clientList = []
        if self.flag == 'Travel':
            self.lmbd = lmbd
            self.mu = mu
            self.inputFlow = InputFlow(self.lmbd)
            self.service_param = self.mu
            self.blockSize = blockSize

            self.doneCustomers : int = 0 

            self.customersList = []
        else: 
            self.lmbd = lmbd 
            self.mu = mu 
            self.inputFlowF = InputFlow(self.lmbd)
            self.inputFlowYu = InputFlow(self.lmbd /10)
            self.service_param = self.mu 
            self.customersList = []
            self.reservedValue = 0
            self.blockSize = blockSize
            

    def oneItteration(self):
        if self.flag == 'Travel':
            if datetime.fromtimestamp(self.time).month  == 1: 
                if datetime.fromtimestamp(self.time).day > 1 and datetime.fromtimestamp(self.time).day <= 10:
                    self.inputFlow = InputFlow(self.lmbd * 10)
                    self.service_param = self.mu * 1000
            elif datetime.fromtimestamp(self.time).month  == 5: 
                if datetime.fromtimestamp(self.time).day > 1 and datetime.fromtimestamp(self.time).day <= 10:
                    self.inputFlow = InputFlow(self.lmbd * 20)
            elif datetime.fromtimestamp(self.time).month  == 7 or datetime.fromtimestamp(self.time).month  == 8: 
                self.inputFlow = InputFlow(self.lmbd * 17)
            elif datetime.fromtimestamp(self.time).month  == 9: 
                if datetime.fromtimestamp(self.time).day > 1 and datetime.fromtimestamp(self.time).day <= 14:
                    self.inputFlow = InputFlow(self.lmbd *18)
            else: 
                self.inputFlow = InputFlow(self.lmbd )
                self.service_param = self.mu
        
            if len(self.customersList) == 0: 
                time = self.inputFlow.get_time()
                self.time += time
                customer = Customer(self.time)
                customer.getEndTime(self.service_param)
                self.customersList.append(customer)
            else: 
                next_event = min(self.customersList, key=attrgetter('endTime'))
                t1 = self.inputFlow.get_time()
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
                    serviceDuration = next_event.endTime
                    next_event.endTime = self.time
                    self.customersList.remove(next_event)
                    self.clientList.append(fillOrderInfo(datetime.fromtimestamp(next_event.startTime), datetime.fromtimestamp(next_event.endTime), serviceDuration, 1,  self.flag)) 

        elif self.flag == 'Med': 
            if len(self.customersList) == 0:
                timeF = self.inputFlowF.get_time()
                timeYu = self.inputFlowYu.get_time()
                minTime = min(timeF, timeYu)

                self.time += minTime
                if minTime == timeF: 
                    customer = Customer(self.time)
                    customer.value = random.randint(1, 5)
                    customer.getEndTime(self.service_param)
                    self.reservedValue += customer.value
                    self.customersList.append(customer)
                else: 
                    customer = Customer(self.time)
                    customer.value = random.randint(20, 50)
                    customer.getEndTime(self.service_param)
                    self.reservedValue += customer.value
                    self.customersList.append(customer)
                print( f'В системе пусто пришла заявка N = {customer.value}, всего занято {self.reservedValue}')
            else: 
                next_event = min(self.customersList, key=attrgetter('endTime'))
                timeF = self.inputFlowF.get_time()
                timeYu = self.inputFlowYu.get_time()
                minTime = min(timeF, timeYu)
                if minTime < next_event.endTime:
                    if minTime == timeF: 
                        value = random.randint(1,5)
                        if self.reservedValue + value <= self.blockSize:
                            customer = Customer(self.time)
                            customer.value = value
                            customer.getEndTime(self.service_param)
                            self.reservedValue += customer.value
                            self.customersList.append(customer)
                            print( f'В системе пусто пришла заявка N = {customer.value}, всего занято {self.reservedValue}')
                    else: 
                        value = random.randint(20,50)
                        if self.reservedValue + value <= self.blockSize:
                            customer = Customer(self.time)
                            customer.value = value
                            customer.getEndTime(self.service_param)
                            self.reservedValue += customer.value
                            self.customersList.append(customer)
                            print( f'В системе пусто пришла заявка N = {customer.value}, всего занято {self.reservedValue}')
                else: 
                    self.time += next_event.endTime
                    serviceDuration = next_event.endTime
                    next_event.endTime = self.time
                    self.reservedValue -= next_event.value
                    self.customersList.remove(next_event)
                    self.clientList.append(fillOrderInfo(datetime.fromtimestamp(next_event.startTime), datetime.fromtimestamp(next_event.endTime), 0, next_event.value, self.flag)) 
       

    def cycle(self): 
        counter = 0 
        while datetime.fromtimestamp(self.time).year != 2023: 
            self.oneItteration()
            counter += 1
        print('done')
        if self.flag == 'Travel':
            listC = sorted(self.clientList, key = attrgetter('StartDate') )
            writeCSV(listC, self.flag)
        else: 
            listC = sorted(self.clientList, key = attrgetter('StartDate') )
            writeCSV(listC, self.flag)