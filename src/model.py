import random 

class InputFlow:
    def __init__(self, parameter):
        self.parameter = parameter
    def get_time(self):
        return random.expovariate(self.parameter)

class Service: 
    def __init__(self, parameter):
        self.parameter = parameter
        self.numberOfCustomers : int = 0
    def get_time(self): 
        return random.expovariate(self.parameter * self.numberOfCustomers)

    def addCustomer(self):
        self.numberOfCustomers += 1 
    
    def removeCustomer(self): 
        self.numberOfCustomers -= 1 

class Buffer: 
    def __init__(self, maxSize):
        self.maxSize =maxSize
        self.numberOfCustomers : int = 0 
    
    def addCustomer(self):
        self.numberOfCustomers += 1 
    
    def removeCustomer(self): 
        self.numberOfCustomers -= 1 

class Model: 
    def __init__(self, lmbd, mu, bufferSize, blockSize):
        self.inputFlow = InputFlow(lmbd)
        self.service = Service(mu)
        self.buffer = Buffer(bufferSize)
        self.blockSize = blockSize
        
        self.customersInSystem : int = 0
        self.doneCustomers : int = 0 

    def oneItteration(self):
        if self.service.numberOfCustomers == 0: 
            time = self.inputFlow.get_time()
            self.service.addCustomer()

            print(f'Time: {time}, arrived customer')
        else: 
            t1 = self.inputFlow.get_time()
            t2 = self.service.get_time()
            if t1 < t2: 
                if self.service.numberOfCustomers + 1 <= self.blockSize:
                    self.service.addCustomer()
                    print(f'Time: {t1}, arrived customer')
                else: 
                    if self.buffer.numberOfCustomers +1 <= self.buffer.maxSize:
                        self.buffer.addCustomer()
                        print(f'Time: {t1}, arrived customer in buffer')
            else: 
                self.service.removeCustomer()
                print(f'Time: {t2}, serviced customer')
            
    def cycle(self): 
        counter = 0 
        while counter != 20: 
            self.oneItteration()
            counter += 1
