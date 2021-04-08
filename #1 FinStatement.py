#import csv
import pandas as pd
#import numpy as np
#store 1

df = pd.read_csv('#1 2020-11.csv', usecols = ['Account', 'Desc', 'BalanceFwd', 'CurrMth', 'YTDBal', 'AcctType', 'GroupType', 'SubType'])


####sales tab###################

Net_Revenue = df.loc[df.GroupType.isin(['110', '120', '140', '150', '160', '170']), 'YTD'].sum()*-1

Cost_of_Revenue = df.loc[df.GroupType.isin(['210', '220', '240', '250', '260', '270']), 'YTD'].sum()

Gross_Profit = Net_Revenue - Cost_of_Revenue

Variable = df.loc[df.GroupType.isin(['10']), 'YTD'].sum()
Personnel = df.loc[df.GroupType.isin(['20']), 'YTD'].sum()
Semi = df.loc[df.GroupType.isin(['30']), 'YTD'].sum()
Fixed = df.loc[df.GroupType.isin(['40']), 'YTD'].sum()

Total_Expenses = Variable + Personnel + Semi + Fixed

Other = df.loc[df.SubType.isin(['81', '91']), 'YTD'].sum()*-1
Dealer = df.loc[df.SubType.isin(['82']), 'YTD'].sum()*-1

#######sales#########
writer = open("#1 numbers.txt", "w")

writer.write(str(Net_Revenue) + "\n\n")
writer.write(str(Cost_of_Revenue) + "\n\n")
writer.write(str(Gross_Profit) + "\n\n\n")


writer.write(str(Variable) + "\n")
writer.write(str(Personnel) + "\n")
writer.write(str(Semi) + "\n")
writer.write(str(Fixed) + "\n")
writer.write(str(Total_Expenses) + "\n\n")

writer.write(str(Gross_Profit - Total_Expenses) + "\n\n")
writer.write(str(Other) + "\n")
writer.write(str(0) + "\n")
writer.write(str(Dealer) + "\n")








