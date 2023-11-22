import random
from .customers_dataclasses import CustomerTravelEleven, CustomerMed
import csv 

listOfCountres = ['Kazakhstan', 'Russia', 'Dominican Republic', 'Italy', 'United Arab Emirates', 'Thailand',
                  'Egypt', 'Turkey', 'Maldives', 'Georgia']
startPriceList = [70000, 40000, 120000, 150000, 147000, 170000, 100000, 
                  120000, 65000, 175000, 67000]
sexList = ['Male', 'Female']
websitePageList = ['Home', 'Order', 'Directions', 'About Us', 'Search', 'Sales']
numberOfPersonList = [1, 2, 3 ,4, 5, 6 ,7, 2, 3, 4 ,12,2 ,1 ,3 ,4 ,5, 2, 2 ,2 ,2 ,2]

categoryList = ["info", 'med_service']

def fillOrderInfo(startDate, EndDate, serviceDuration, value,  flag):
    if flag == 'Travel':
        rnd = random.randint(0, len(listOfCountres)-1)
        sex = random.randint(0,1)
        sex = sexList[sex]
        if random.randint(0,1) == 1: 
            consultation = True
            serviceDuration = int(serviceDuration/60) - random.randint(0, int(serviceDuration/60))
            if serviceDuration < 1: 
                consultation = False
                serviceDuration = 0 
        else:
            consultation = False
            serviceDuration = 0
        websitePage = websitePageList[random.randint(0, len(websitePageList)-1)]
        numberPerson = random.randint(1, 5)
        totalBill =(startPriceList[rnd] * numberPerson ) * (100 - random.randint(0, 27))/100

        if consultation == True:
            totalBill = totalBill * (100 - random.randint(0, 12))/100
        return CustomerTravelEleven(random.randint (0, 10E3),numberPerson,listOfCountres[rnd],
                                    sex, startDate.replace(microsecond=0), EndDate.replace(microsecond=0), int(totalBill), consultation, websitePage, serviceDuration)
    elif flag == 'Med':
        sex = random.randint(0,1)
        sex = sexList[sex]
        if value <20: 
            categoryP = 'individual'
        else: 
            categoryP = 'The business'

        vote = random.randint(1,5)

        if value == 1: 
            value = random.randint(-1,1)
        if value == 0:
            service_category = categoryList[0]
        elif value > 0: 
            service_category = categoryList[1]
        else: 
            service_category = categoryList[random.randint(0,1)]
        
        return CustomerMed(random.randint (0, 10E3), categoryP, service_category, value, sex, vote,  startDate.replace(microsecond=0), EndDate.replace(microsecond=0))




def writeCSV(customerList, flag): 
    if flag == 'Travel':
        row = ['id','start_session','stop_session','sex','travel_country','number_of_travalers'
                              , 'consultation', 'website_page', 'cons_duration (min)', 'travel_amount']
        with open('out' + flag + '.csv','w') as out_csv:
            file_writer = csv.writer(out_csv, delimiter=';', lineterminator="\r")
            file_writer.writerow(row)
            for customer in customerList: 
                file_writer.writerow([customer.id, customer.StartDate, customer.EndDate, customer.sex,
                                    customer.direction, customer.numberPerson, customer.consultation,
                                    customer.websitePage,customer.consultationDuration, customer.totalBill])
        print('Travel done')
    else: 
         row = ['id','start_session','stop_session','sex', 'service_category', 
                'customer_category', 'number_person','assesment']
         with open('out' + flag + '.csv','w') as out_csv:
            file_writer = csv.writer(out_csv, delimiter=';', lineterminator="\r")
            file_writer.writerow(row)
            for customer in customerList: 
                file_writer.writerow([customer.id, customer.StartDate, customer.EndDate, customer.sex,
                                    customer.serviceCategory, customer.category, customer.numberPerson,
                                    customer.vote])