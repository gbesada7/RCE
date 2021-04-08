#import csv
import pandas as pd

#store 1

df = pd.read_csv('#1 BS 2021-2.csv', usecols = ['Account', 'Desc', 'BalanceFwd', 'CurrMth', 'YTDBal', 'AcctType', 'GroupType', 'SubType'])

Cash = df.loc[df.Account.isin(['200','200S','201','201A','201B','203','205C','225','226','226Q','202',
                               '202P','202S','202T','204','204A','204B','204C','204D','204RC',]), 'YTDBal'].sum() 

CIT = df.loc[df.SubType.isin(['A3']), 'YTDBal'].sum()

Trade = df.loc[df.SubType.isin(['B1']), 'YTDBal'].sum()

Fin_Warr_Fact_Other = df.loc[df.SubType.isin(['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B9']), 'YTDBal'].sum()

Intercompany = df.loc[df.SubType.isin(['H1', 'H2']), 'YTDBal'].sum()

Total_Current1 = Cash + CIT + Trade + Fin_Warr_Fact_Other + Intercompany 

Inventories = df.loc[df.GroupType.isin(['C']), 'YTDBal'].sum()

Loaners1 = df.loc[df.SubType.isin(['D2']), 'YTDBal'].sum()

Prepaid_exp_other = df.loc[df.SubType.isin(['D1', 'D3']), 'YTDBal'].sum()




Total_Current2 = Total_Current1 + Loaners1 + Prepaid_exp_other + Inventories

PPE = df.loc[df.GroupType.isin(['G']), 'YTDBal'].sum()

Other_Noncurrent = df.loc[df.Account.isin(['2296']), 'YTDBal'].sum()

Goodwill = df.loc[df.SubType.isin(['H3']), 'YTDBal'].sum()

Total_Assets = Total_Current2 + PPE + Other_Noncurrent + Goodwill
                          

                          
######################liabilities##############################

Notes_Payable = df.loc[df.Account.isin(['310', '311', '314N']), 'YTDBal'].sum()*-1
Current_lt_Debt = df.loc[df.SubType.isin(['AA3']), 'YTDBal'].sum()*-1
Trade_AP = df.loc[df.SubType.isin(['AA1']), 'YTDBal'].sum()*-1

Accrued_exp = df.loc[df.Account.isin(['205A','319', '319F','319M','319T','321','321A','321E','321G','321GS','321H','321K',
'321P','321S','321Y','322A','322D','322E','322F','322G','322S','322W','329',
'323','323A','323B','323F','323S','324','324A','324B','324H','324L','324P',
'324R','324S','324T','325','326','328','1','300A','300B','300C','300Z','301','301F','301M','301T','314','314U','320',
'331','331G','331P','330','331R','331S','331T','343',
'344','344C','332','342','342H','302A','302B','302C',
'302D','302E','302F','302G','302H','302L','302S','302U',
'302V','303A','303B','303C','303D','303E','303F','303G',
'303H','303L','303U','300E','300G','300HC','300J','300L',
'300M','300N','300P','300PA','300R','300RA','300SR','300W',
'300WF','300WL','305','305A','305B','305C','305D','305E',]), 'YTDBal'].sum()*-1
                          
Loaners2 = df.loc[df.Account.isin(['312', '313']), 'YTDBal'].sum()*-1
Intercompany_payables = df.loc[df.SubType.isin(['AA8']), 'YTDBal'].sum()*-1

Total_Current_Liab = (Notes_Payable + Current_lt_Debt + Trade_AP + Accrued_exp + Loaners2 + Intercompany_payables)

Long_Term_Liab = df.loc[df.SubType.isin(['BB1', 'BB2']), 'YTDBal'].sum()*-1

###################################equity######################

Common_Stock = df.loc[df.Account.isin(['360']), 'YTDBal'].sum()*-1

PIC = df.loc[df.Account.isin(['365']), 'YTDBal'].sum()*-1

Retained_Earnings = df.loc[df.Account.isin(['370',]), 'YTDBal'].sum()*-1

Dividends = df.loc[df.Account.isin(['375']), 'YTDBal'].sum()*-1
P_L = df.loc[df.Desc.isin(['Profit and Loss']), 'YTDBal'].sum()*-1
                                                                        
########write##############
writer = open("#1 numbers.txt", "w")

writer.write(str(Cash) + "\n")
writer.write(str(CIT) + "\n\n")
writer.write(str(Trade) + "\n")
writer.write(str(Fin_Warr_Fact_Other)+ "\n")
writer.write(str(Intercompany) + "\n")
writer.write(str(Total_Current1) + "\n\n")

writer.write(str(Inventories) + "\n")
writer.write(str(Loaners1) + "\n")
writer.write(str(Prepaid_exp_other) + "\n")
writer.write(str(Total_Current2) + "\n\n")

writer.write(str(PPE) + "\n")
writer.write(str(Other_Noncurrent) + "\n")
writer.write(str(Goodwill) + "\n\n")
writer.write(str(Total_Assets) + "\n\n\n\n\n")

writer.write(str(Notes_Payable) + "\n")
writer.write(str(Current_lt_Debt) + "\n")
writer.write(str(Trade_AP) + "\n")
writer.write(str(Accrued_exp) + "\n")
writer.write(str(Loaners2) + "\n")
writer.write(str(Intercompany_payables) + "\n")
writer.write(str(Total_Current_Liab) + "\n\n\n")
writer.write(str(Long_Term_Liab) + "\n\n\n")
writer.write(str(Common_Stock) + "\n")
writer.write(str(PIC) + "\n")
writer.write(str(P_L+Retained_Earnings+Dividends) + "\n")



