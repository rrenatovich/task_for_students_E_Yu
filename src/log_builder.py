import random
from .customers_dataclasses import CustomerTravelEleven
import csv 

listOfCountres = ['Kazakhstan', 'Russia', 'Dominican Republic', 'Italy', 'United Arab Emirates', 'Thailand']
startPriceList = [70000, 40000, 120000, 150000, 147000, 170000, 100000]
sexList = ['Male', 'Female']
websitePageList = ['Home', 'Order', 'Directions', 'About Us']
numberOfPersonList = [1, 2, 3 ,4, 5, 6 ,7, 2, 3, 4 ,12,2 ,1 ,3 ,4 ,5, 2, 2 ,2 ,2 ,2]


def fillOrderInfo(startDate, EndDate):
    rnd = random.randint(0, len(listOfCountres)-1)
    sex = random.randint(0,1)
    numberPerson = random.randint(1, 5)
    totalBill =(startPriceList[rnd] * numberPerson ) * (100 - random.randint(0, 27))/100
    return CustomerTravelEleven(random.randint (0, 10E6),numberPerson,listOfCountres[rnd],
                                 sex, startDate, EndDate, totalBill, 'PASS', 'PASS', 'PASS')



def writeCSV(customerList): 
    with open('out.csv', 'w') as out_csv:
        file_writer = csv.writer(out_csv, delimiter=';', lineterminator="\r")
        file_writer.writerow(['id','start_session','stop_session','sex','travel_country','number_of_travalers',
                             'travel_date', 'consultation', 'website_page', 'cons_duration', 'travel_amount'])
        for customer in customerList: 
            file_writer.writerow([customer.id, customer.StartDate, customer.EndDate, customer.sex,
                                  customer.direction, customer.numberPerson, 'PASS', customer.consultation,
                                   customer.websitePage,customer.consultationDuration, customer.totalBill])
