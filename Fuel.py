import math
import pandas as pd
import decimal
#fuel

#note:
#Change name of Current Odometer to VIN manually
#Change used recon if any stores are in unassigned


def round_up(number:float, decimals:int=2):
    math.ceil(number)
    factor = 10 ** decimals
    
    return math.ceil(number*factor)/factor

def round_down(number:float, decimals:int = 2):
    factor = 10**decimals
    return math.floor(number*factor)/factor
        
        

df = pd.read_csv('QT 2021-3-31.csv', usecols = ['Emboss Line 2', 'Department', 'Posted Date', 
                                             'Transaction Date', 'Transaction Time', 'Transaction Ticket Number', 
                                             'Driver Last Name', 'DriverDepartment', 'Units', 'Unit Cost', 'Total Fuel Cost', 'VIN', 
                                             'Merchant Site ID', 'Merchant Name', 'Merchant Street Address', 'Merchant City', 
                                             'Merchant State / Province', 'Merchant Postal Code', 'Product', 'Transaction Description', 
                                             'Transaction Device'])
#df.dropna(subset = ['Account Number', 'Account Name',  'Card Number'])
#df.rename({'Current Odometer': 'VIN'}, axis = 'columns')# change name to VIn?
#df.rename(columns = {'Driver Department': 'x', 'Driver Department': 'y'}) # change name to VIn?


H9_Sales1 = df.loc[df.Department.isin(['#9 Hyundai Sales']), 'Total Fuel Cost'].sum()
H9_Sales2 = df.loc[df.Department.isin(['#9 Sales']), 'Total Fuel Cost'].sum()
H9_Service = df.loc[df.Department.isin(['#9 Hyundai Service']), 'Total Fuel Cost'].sum()
H9_Parts1 = df.loc[df.Department.isin(['#9 Parts']), 'Total Fuel Cost'].sum()
H9_Parts2 = df.loc[df.Department.isin(['Duluth Parts Driver']), 'Total Fuel Cost'].sum()

Mazda_Sales1 = df.loc[df.Department.isin(['#10 Sales']), 'Total Fuel Cost'].sum()
Mazda_Sales2 = df.loc[df.Department.isin(['Mazda Sales']), 'Total Fuel Cost'].sum()
Mazda_Service = df.loc[df.Department.isin(['Mazda Service']), 'Total Fuel Cost'].sum()
Mazda_Parts = df.loc[df.Department.isin(['Mazda Parts']), 'Total Fuel Cost'].sum()

H16_Sales1 = df.loc[df.Department.isin(['#16 Hyundai Sales']), 'Total Fuel Cost'].sum()
H16_Sales2 = df.loc[df.Department.isin(['#16 Sales']), 'Total Fuel Cost'].sum()
H16_Service = df.loc[df.Department.isin(['#16 Service']), 'Total Fuel Cost'].sum()
H16_Parts1 = df.loc[df.Department.isin(['#16 Parts']), 'Total Fuel Cost'].sum()
H16_Parts2 = df.loc[df.Department.isin(['Roswell Parts Drive']), 'Total Fuel Cost'].sum()

Audi_Sales1 = df.loc[df.Department.isin(['Audi Sales']), 'Total Fuel Cost'].sum()
Audi_Sales2 =df.loc[df.Department.isin(['#17 Sales']), 'Total Fuel Cost'].sum()
Audi_Service = df.loc[df.Department.isin(['#17 Service']), 'Total Fuel Cost'].sum()
Audi_Parts = df.loc[df.Department.isin(['#17 Parts']), 'Total Fuel Cost'].sum()

Kia_Sales = df.loc[df.Department.isin(['Kia Sales']), 'Total Fuel Cost'].sum()
Kia_Service = df.loc[df.Department.isin(['Kia Service']), 'Total Fuel Cost'].sum()
Kia_Parts = df.loc[df.Department.isin(['#18 Parts']), 'Total Fuel Cost'].sum()

Used_Recon = df.loc[df.DriverDepartment.isin(['Used Recon']), 'Total Fuel Cost'].sum()
Cleve = df.loc[df.DriverDepartment.isin(['Unassigned']), 'Total Fuel Cost'].sum()
    
New_9 = (H9_Sales1+H9_Sales2)/2
Used_9 = (H9_Sales1+H9_Sales2)/2

New_9 = round_up(New_9)
Used_9 = round_up(Used_9)
if ((H9_Sales1+H9_Sales2)*100 % 2) > 0:
    Used_9 = Used_9-.01

Parts_9 = H9_Parts1+H9_Parts2

New_10 = (Mazda_Sales1+Mazda_Sales2)/2

Used_10 = (Mazda_Sales1+Mazda_Sales2)/2

New_10 = round_up(New_10)
Used_10 = round_up(Used_10)
if((Mazda_Sales1+Mazda_Sales2)*100 % 2) > 0:
    Used_10 = Used_10-.01

Roswell_Parts = H16_Parts1 + H16_Parts2

New_17 = (Audi_Sales1+Audi_Sales2)/2
Used_17 = (Audi_Sales1+Audi_Sales2)/2
New_17 = round_up(New_17)
Used_17 = round_up(Used_17)

if ((Audi_Sales1+Audi_Sales2)*100 % 2) > 0:
    Used_17 = Used_17-.01

Kia_Sales2 = Kia_Sales/2
Kia_Sales1 = Kia_Sales/2
Kia_Sales2 = round_up(Kia_Sales2)
Kia_Sales1 = round_up(Kia_Sales1)

if ((Kia_Sales)*100 % 2) > 0:##if odd
    Used_18 = Kia_Sales1-.01
    New_18 = Kia_Sales/2
    



writer = open("Fuel Numbers.txt", "w")

writer.write(str(New_9) + "\n")
writer.write(str(Used_9) + "\n")
writer.write(str(H9_Service) + "\n")
writer.write(str(Parts_9) + "\n")

writer.write(str(New_10) + "\n")
writer.write(str(Used_10) + "\n")
writer.write(str(Mazda_Service)+ "\n")
writer.write(str(Mazda_Parts) + "\n")

writer.write(str(H16_Sales1) + "\n")
writer.write(str(H16_Sales2) + "\n")
writer.write(str(H16_Service) + "\n")
writer.write(str(Roswell_Parts) + "\n")

writer.write(str(New_17) + "\n")
writer.write(str(Used_17) + "\n")
writer.write(str(Audi_Service) + "\n")
writer.write(str(Audi_Parts) + "\n")

writer.write(str(New_18) + "\n")
writer.write(str(Used_18) + "\n")
writer.write(str(Kia_Service) + "\n")
writer.write(str(Kia_Parts) + "\n\n")



writer.write(str(Cleve) + "\n")
writer.write(str(Used_Recon) + "\n")

