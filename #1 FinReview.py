#import csv
import pandas as pd
#import numpy as np
#store 1

df = pd.read_csv('#1 2021-2.csv', usecols = ['Account', 'Desc', 'BalanceFwd', 'CurrMth', 'YTDBal', 'GroupType', 'SubType'])


####sales tab###################
Bfwd_total = df['BalanceFwd'].sum()

New_Sales_Total = df.loc[df['GroupType'] == 110, 'CurrMth'].sum()*-1
Used_Sales_Total = df.loc[df['GroupType'] == 120, 'CurrMth'].sum()*-1

Total_Sales = (New_Sales_Total + Used_Sales_Total)



Gross_New = df.loc[df.SubType.isin(['111', '211',]), 'CurrMth'].sum()*-1
HTB_Op_Support = df.loc[df.Account.isin(['804']), 'CurrMth'].sum()*-1
Marketing_Allowance = df.loc[df.Account.isin(['905D']), 'CurrMth'].sum()*-1

Total_Op_Support = (HTB_Op_Support + Marketing_Allowance)

Gross_New_FI = df.loc[df.SubType.isin(['114', '214']), 'CurrMth'].sum()*-1

Gross_Used = df.loc[df.SubType.isin(['121', '221']), 'CurrMth'].sum()*-1
Gross_Used_FI = df.loc[df.SubType.isin(['124', '224']), 'CurrMth'].sum()*-1
Gross_Wholesale = df.loc[df.SubType.isin(['126', '226']), 'CurrMth'].sum()*-1


Gross_New_Total = (Gross_New + Total_Op_Support + Gross_New_FI)
Gross_Used_Total = (Gross_Used + Gross_Used_FI + Gross_Wholesale)

Gross_Total = (Gross_New_Total + Gross_Used_Total)

Sales_Variable= df.loc[df.Account.isin(['13A','14A','15A','19A','56A','57A','58A','59A','13B','14B',
                                        '15B','19B','56B','57B','58B','59B',]), 'CurrMth'].sum()
Sales_Personnel = df.loc[df.Account.isin(['10A','11A','12A','16A','17A','18A','20A','21A','22A','23A','24A',
                                          '25A','26A','27A','28A','29A','30A','10B','11B','12B','16B','17B',
                                          '18B','20B','21B','22B','23B','24B','25B','26B','27B','28B','29B',
                                          '30B', '39A', '39B']), 'CurrMth'].sum()
Sales_Semi = df.loc[df.Account.isin(['31A','32A','34A','35A','36A','37A','38A','40A','41A','42A',
                                     '43A','44A','45A','46A','47A','48A','49A','51A','52A','53A','54A','55A',
                                     '60A','61A','62A','63A','64A','66A','68A','70A','71A','72A','73A','74A',
                                     '75A','76A','31B','32B','34B','35B',
                                     '36B','37B','38B','40B','41B','42B',
                                     '43B','44B','45B','46B','47B','48B','49B','51B','52B','53B','54B','55B',
                                     '60B','61B','62B','63B','64B','66B','68B','70B','71B','72B','73B','74B','75B','76B',
                                     '78A',	'78B',]), 'CurrMth'].sum()
Sales_Fixed = df.loc[df.Account.isin(['80A','81A','82A','84A','85A','86A','87A','88A','89A','90A',
                                      '91A','92A','80B','81B','82B','84B','85B','86B','87B','88B','89B',
                                      '90B','91B','92B',]), 'CurrMth'].sum()

Total_Sales_Expense = (Sales_Variable + Sales_Personnel + Sales_Semi + Sales_Fixed)

Operating_Inc_Sales = (Gross_Total - Total_Sales_Expense)


Comp_Draws = df.loc[df.Account.isin(['10A', '10B']), 'CurrMth'].sum()
#Comp_RCE = df.loc[df.SubType.isin(['20F']), 'CurrMth'].sum()
Comp_Sales = df.loc[df.Account.isin(['11A', '11B']), 'CurrMth'].sum()
Comp_Spiffs = df.loc[df.Account.isin(['17A', '17B']), 'CurrMth'].sum() 
#Comp_GM = df.loc[df.Account.isin(['20A', '20B']), 'CurrMth'].sum()
Comp_Supervision = df.loc[df.Account.isin(['21A', '21B']), 'CurrMth'].sum()
Comp_Salaries_Clerical = df.loc[df.Account.isin(['22A', '22B']), 'CurrMth'].sum()
Comp_Other = df.loc[df.Account.isin(['23A', '23B']), 'CurrMth'].sum()

Comp_FI = df.loc[df.Account.isin(['12A', '12B']), 'CurrMth'].sum()

Total_Sales_Comp = (Comp_Draws + Comp_Sales + Comp_Spiffs + Comp_Supervision + Comp_Salaries_Clerical
                    + Comp_Other+Comp_FI)
#####service###############

Serv_Cus_Pay = df.loc[df.Account.isin(['460']), 'CurrMth'].sum()*-1
Serv_Warr = df.loc[df.Account.isin(['462', '463P']), 'CurrMth'].sum()*-1
Serv_Internal = df.loc[df.Account.isin(['463', '463A', '463U']), 'CurrMth'].sum()*-1
Serv_Sublet = df.loc[df.Account.isin(['466', '466I']), 'CurrMth'].sum()*-1

Gross_Serv_Cus_Pay = df.loc[df.Account.isin(['460', '660']), 'CurrMth'].sum()*-1
Gross_Serv_Warr = df.loc[df.Account.isin(['462', '463P', '662', '663P']), 'CurrMth'].sum()*-1
Gross_Serv_Internal = df.loc[df.Account.isin(['463', '463A', '463U', '663', '663A', '663U']), 'CurrMth'].sum()*-1
Gross_Serv_Sublet = df.loc[df.Account.isin(['466', '466I', '666']), 'CurrMth'].sum()*-1
Gross_Serv_Unapplied = df.loc[df.Account.isin(['665']), 'CurrMth'].sum()*-1



Service_Variable = df.loc[df.Account.isin(['13D','14D','15D','19D','56D','57D','58D','59D',]), 'CurrMth'].sum()
Service_Personnel = df.loc[df.Account.isin(['10D','11D','12D','16D','17D','18D','20D','21D',
                                            '22D','23D','24D','25D','26D','27D','28D','29D','30D', '39D']), 'CurrMth'].sum()
Service_Semi = df.loc[df.Account.isin(['31D','32D','34D','35D','36D','37D','38D','40D','41D','42D',
                                       '43D','44D','45D','46D','47D','48D','49D','51D','52D','53D','54D',
                                       '55D','60D','61D','62D','63D','64D','66D','68D','70D','71D','72D',
                                       '73D','74D','75D','76D', '78D']), 'CurrMth'].sum()
Service_Fixed = df.loc[df.Account.isin(['80D','81D','82D','84D','85D','86D','87D',
                                        '88D','89D','90D','91D','92D',]), 'CurrMth'].sum()

Serv_Comp_Draws = df.loc[df.Account.isin(['10D']), 'CurrMth'].sum()
#Comp_RCE = df.loc[df.SubType.isin(['20F']), 'CurrMth'].sum()
Serv_Comp_Sales = df.loc[df.Account.isin(['11D',]), 'CurrMth'].sum()
Serv_Comp_Spiffs = df.loc[df.Account.isin(['17D',]), 'CurrMth'].sum() 
#Serv_Comp_GM = df.loc[df.Account.isin(['20D']), 'CurrMth'].sum()
Serv_Comp_Supervision = df.loc[df.Account.isin(['21D',]), 'CurrMth'].sum()
Serv_Comp_Salaries_Clerical = df.loc[df.Account.isin(['22D',]), 'CurrMth'].sum()
Serv_Comp_Other = df.loc[df.Account.isin(['23D']), 'CurrMth'].sum()



Total_Serv_Comp = (Serv_Comp_Draws + Serv_Comp_Sales + Serv_Comp_Spiffs + Serv_Comp_Supervision + 
                   Serv_Comp_Salaries_Clerical + Serv_Comp_Other)

####express######################

Express_Cus_Pay = df.loc[df.Account.isin(['460E']), 'CurrMth'].sum()*-1
Express_Warr = df.loc[df.Account.isin(['462E']), 'CurrMth'].sum()*-1
Express_Internal = df.loc[df.Account.isin(['463AQ', '463E', '463Q']), 'CurrMth'].sum()*-1

Gross_Express_Cus_Pay = df.loc[df.Account.isin(['460E', '660E']), 'CurrMth'].sum()*-1
Gross_Express_Warr = df.loc[df.Account.isin(['462E', '662E',]), 'CurrMth'].sum()*-1
Gross_Express_Internal = df.loc[df.Account.isin(['463AQ','463E', '463Q', '663AQ','663E','663Q',]), 'CurrMth'].sum()*-1

Express_Variable = df.loc[df.Account.isin(['13Q','14Q','15Q','19Q','56Q','57Q','58Q','59Q',]), 'CurrMth'].sum()
Express_Personnel = df.loc[df.Account.isin(['10Q','11Q','12Q','16Q','17Q','18Q','20Q','21Q','22Q','23Q',
                                            '24Q','25Q','26Q','27Q','28Q','29Q','30Q',]), 'CurrMth'].sum()
Express_Semi = df.loc[df.Account.isin(['31Q','32Q','34Q','35Q','36Q','37Q','38Q', '39Q', '40Q','41Q','42Q',
                                       '43Q','44Q','45Q','46Q','47Q','48Q','49Q','51Q','52Q','53Q','54Q',
                                       '55Q','60Q','61Q','62Q','63Q','64Q','66Q','68Q','70Q','71Q','72Q',
                                       '73Q','74Q','75Q','76Q', '78Q',]), 'CurrMth'].sum()
Express_Fixed = df.loc[df.Account.isin(['80Q','81Q','82Q','84Q','85Q','86Q','87Q','88Q',
                                        '89Q','90Q','91Q','92Q',]), 'CurrMth'].sum()

Express_Comp_Draws = df.loc[df.Account.isin(['10Q']), 'CurrMth'].sum()
#Comp_RCE = df.loc[df.SubType.isin(['20F']), 'CurrMth'].sum()
Express_Comp_Sales = df.loc[df.Account.isin(['11Q',]), 'CurrMth'].sum()
Express_Comp_Spiffs = df.loc[df.Account.isin(['17Q',]), 'CurrMth'].sum() 
#Express_Comp_GM = df.loc[df.Account.isin(['20Q']), 'CurrMth'].sum()
Express_Comp_Supervision = df.loc[df.Account.isin(['21Q',]), 'CurrMth'].sum()
Express_Comp_Salaries_Clerical = df.loc[df.Account.isin(['22Q',]), 'CurrMth'].sum()
Express_Comp_Other = df.loc[df.Account.isin(['23Q']), 'CurrMth'].sum()

Total_Express_Comp = (Express_Comp_Draws + Express_Comp_Sales + Express_Comp_Spiffs + Express_Comp_Supervision + 
                   Express_Comp_Salaries_Clerical + Express_Comp_Other)

#####Body Shop####################

BodyShop_Cus_Pay = df.loc[df.Account.isin(['460C']), 'CurrMth'].sum()*-1
BodyShop_Warr = df.loc[df.Account.isin(['462C']), 'CurrMth'].sum()*-1
BodyShop_Internal = df.loc[df.Account.isin(['463C']), 'CurrMth'].sum()*-1
BodyShop_Sublet = df.loc[df.Account.isin(['466C','466P']), 'CurrMth'].sum()*-1
BodyShop_Materials = df.loc[df.Account.isin(['466T','477C']), 'CurrMth'].sum()*-1

Gross_BodyShop_Cus_Pay = df.loc[df.Account.isin(['460C', '660C']), 'CurrMth'].sum()*-1
Gross_BodyShop_Warr = df.loc[df.Account.isin(['462C', '662C']), 'CurrMth'].sum()*-1
Gross_BodyShop_Internal = df.loc[df.Account.isin(['463C', '663C']), 'CurrMth'].sum()*-1
Gross_BodyShop_Sublet = df.loc[df.Account.isin(['466C','466P', '666C', '666P']), 'CurrMth'].sum()*-1
Gross_BodyShop_Materials = df.loc[df.Account.isin(['466T','477C', '677C']), 'CurrMth'].sum()*-1
Gross_BodyShop_Unapplied = df.loc[df.Account.isin(['665C']), 'CurrMth'].sum()*-1

BodyShop_Variable = df.loc[df.Account.isin(['13E','14E','15E','19E','56E','57E','58E','59E',]), 'CurrMth'].sum()
BodyShop_Personnel = df.loc[df.Account.isin(['10E','11E','12E','16E','17E','18E','20E','21E',
                                             '22E','23E','24E','25E','26E','27E','28E','29E','30E',]), 'CurrMth'].sum()
BodyShop_Semi = df.loc[df.Account.isin(['31E','32E','34E','35E','36E','37E','38E','40E','41E','42E',
                                        '43E','44E','45E','46E','47E','48E','49E','51E','52E','53E','54E',
                                        '55E','60E','61E','62E','63E','64E','66E','68E','70E','71E','72E',
                                        '73E','74E','75E','76E','78E',]), 'CurrMth'].sum()
BodyShop_Fixed = df.loc[df.Account.isin(['80E','81E','82E','84E','85E','86E','87E','88E',
                                         '89E','90E','91E','92E',]), 'CurrMth'].sum()


BodyShop_Comp_Draws = df.loc[df.Account.isin(['10E']), 'CurrMth'].sum()
#Comp_RCE = df.loc[df.SubType.isin(['20F']), 'CurrMth'].sum()
BodyShop_Comp_Sales = df.loc[df.Account.isin(['11E',]), 'CurrMth'].sum()
BodyShop_Comp_Spiffs = df.loc[df.Account.isin(['17E',]), 'CurrMth'].sum() 
#BodyShop_Comp_GM = df.loc[df.Account.isin(['20E']), 'CurrMth'].sum()
BodyShop_Comp_Supervision = df.loc[df.Account.isin(['21E',]), 'CurrMth'].sum()
BodyShop_Comp_Salaries_Clerical = df.loc[df.Account.isin(['22E',]), 'CurrMth'].sum()
BodyShop_Comp_Other = df.loc[df.Account.isin(['23E']), 'CurrMth'].sum()



Total_BodyShop_Comp = (BodyShop_Comp_Draws + BodyShop_Comp_Sales + BodyShop_Comp_Spiffs + BodyShop_Comp_Supervision + 
                   BodyShop_Comp_Salaries_Clerical + BodyShop_Comp_Other)

#########Parts################################
Parts_Cus_Pay = df.loc[df.Account.isin(['467','467S','468',]), 'CurrMth'].sum()*-1
Parts_Express = df.loc[df.Account.isin(['467E','480E','481E','485Q','491E','492E']), 'CurrMth'].sum()*-1
Parts_BodyShop = df.loc[df.Account.isin(['467C', '467D']), 'CurrMth'].sum()*-1
Parts_Warranty = df.loc[df.Account.isin(['484', '480']), 'CurrMth'].sum()*-1
Parts_Internal = df.loc[df.Account.isin(['481','485','485A']), 'CurrMth'].sum()*-1
Parts_Counter = df.loc[df.Account.isin(['482', '482A']), 'CurrMth'].sum()*-1
Parts_Wholesale = df.loc[df.Account.isin(['483','483B',]), 'CurrMth'].sum()*-1
Parts_Tires = df.loc[df.Account.isin(['492']), 'CurrMth'].sum()*-1
Parts_Gas = df.loc[df.Account.isin(['491']), 'CurrMth'].sum()*-1

Gross_Parts_Cus_Pay = df.loc[df.Account.isin(['467','467S','468', '667','667S','668',]), 'CurrMth'].sum()*-1
Gross_Parts_Express = df.loc[df.Account.isin(['467E','480E','481E','485Q','491E','492E', '667E','680E',
                                              '681E','685Q','691E','692E']), 'CurrMth'].sum()*-1
Gross_Parts_BodyShop = df.loc[df.Account.isin(['467C', '467D', '667C','667D',]), 'CurrMth'].sum()*-1
Gross_Parts_Warr = df.loc[df.Account.isin(['484', '480', '684','680']), 'CurrMth'].sum()*-1
Gross_Parts_Internal = df.loc[df.Account.isin(['481','485','485A', '681','685','685A']), 'CurrMth'].sum()*-1
Gross_Parts_Counter = df.loc[df.Account.isin(['482', '482A', '682','682A']), 'CurrMth'].sum()*-1
Gross_Parts_Wholesale = df.loc[df.Account.isin(['483','483B','683','683B','687']), 'CurrMth'].sum()*-1
Gross_Parts_Tires = df.loc[df.Account.isin(['492', '692']), 'CurrMth'].sum()*-1
Gross_Parts_Gas = df.loc[df.Account.isin(['491', '691']), 'CurrMth'].sum()*-1
Gross_Parts_Allowance = df.loc[df.Account.isin(['688']), 'CurrMth'].sum()*-1
Gross_Parts_Disc = df.loc[df.Account.isin(['689']), 'CurrMth'].sum()*-1


Parts_Variable = df.loc[df.Account.isin(['13F','14F','15F','19F','56F','57F','58F','59F', '15W']), 'CurrMth'].sum()
Parts_Personnel = df.loc[df.Account.isin(['10F','11F','12F','16F','17F','18F','20F','21F','22F',
                                          '23F','24F','25F','26F','27F','28F','29F','30F', 
                                          '17W', '18W', '20W', '21W', '22W', '23W', '24W', 
                                          '25W', '26W', '27W', '28W', '29W']), 'CurrMth'].sum()
Parts_Semi = df.loc[df.Account.isin(['31F','32F','34F','35F','36F','37F','38F','40F','41F','42F',
                                     '43F','44F','45F','46F','47F','48F','49F','51F','52F','53F','54F',
                                     '55F','60F','61F','62F','63F','64F','66F','68F','70F','71F','72F',
                                     '73F','74F','75F','76F', '77F', '78F', '31W','32W','34W','36W','37W','45W',
                                     '49W','51W','52W','53W','54W','55W','60W','61W','64W','66W','68W',
                                     '71W','72W','73W','74W','75W',]), 'CurrMth'].sum()
Parts_Fixed = df.loc[df.Account.isin(['80F','81F','82F','84F','85F','86F',
                                      '87F','88F','89F','90F','91F','92F',]), 'CurrMth'].sum()

Parts_Comp_Draws = df.loc[df.Account.isin(['10F']), 'CurrMth'].sum()
#Comp_RCE = df.loc[df.SubType.isin(['20F']), 'CurrMth'].sum()
Parts_Comp_Sales = df.loc[df.Account.isin(['11F',]), 'CurrMth'].sum()
Parts_Comp_Spiffs = df.loc[df.Account.isin(['17F',]), 'CurrMth'].sum() 
#Parts_Comp_GM = df.loc[df.Account.isin(['20F']), 'CurrMth'].sum()
Parts_Comp_Supervision = df.loc[df.Account.isin(['21F',]), 'CurrMth'].sum()
Parts_Comp_Salaries_Clerical = df.loc[df.Account.isin(['22F',]), 'CurrMth'].sum()
Parts_Comp_Other = df.loc[df.Account.isin(['23F']), 'CurrMth'].sum()



Total_Parts_Comp = (Parts_Comp_Draws + Parts_Comp_Sales + Parts_Comp_Spiffs + Parts_Comp_Supervision + 
                   Parts_Comp_Salaries_Clerical + Parts_Comp_Other)


########80-90#################

Other_Income = df.loc[df.Account.isin(['900','905','905AD','905E','905G','905R','905W','907','955','955I']), 'CurrMth'].sum()*-1
Dealer_Fees = df.loc[df.Account.isin(['904']), 'CurrMth'].sum()*-1

#########################output########################

#######sales#########
writer = open("#1 numbers.txt", "w")
writer.write((str(New_Sales_Total)) + "\n")
writer.write((str(Used_Sales_Total)) + "\n\n")

writer.write((str(Total_Sales)) + "\n\n")

writer.write((str(Gross_New_Total)) + "\n")
writer.write((str(Gross_Used_Total)) + "\n\n")

writer.write((str(Gross_Total)) + "\n\n")

writer.write((str(Sales_Variable)) + "\n")
writer.write((str(Sales_Personnel)) + "\n")
writer.write((str(Sales_Semi)) + "\n")
writer.write((str(Sales_Fixed)) + "\n\n")

writer.write((str(Total_Sales_Expense)) + "\n\n")

writer.write((str(Operating_Inc_Sales)) + "\n\n\n\n")

writer.write((str(Gross_New)) + "\n")
writer.write((str(Gross_New_FI)) + "\n")
writer.write((str(Total_Op_Support)) + "\n")
writer.write((str(Gross_New_Total)) + "\n\n\n")


writer.write((str(Gross_Used)) + "\n")
writer.write((str(Gross_Used_FI)) + "\n")
writer.write((str(Gross_Used+Gross_Used_FI)) + "\n\n")
writer.write((str(Gross_Wholesale)) + "\n")
writer.write(str(Gross_Used+Gross_Used_FI+Gross_Wholesale) + "\n\n")

writer.write(str(Gross_New_Total + Gross_Used_Total) + "\n\n\n")


writer.write((str(HTB_Op_Support)) + "\n")
writer.write((str(Marketing_Allowance)) + "\n\n")

writer.write((str(Total_Op_Support)) + "\n\n\n\n\n\n\n\n\n\n\n\n\n")

writer.write((str(Comp_Draws)) + "\n")
writer.write((str(Comp_Sales)) + "\n")
writer.write((str(Comp_FI)) + "\n")
writer.write((str(Comp_Spiffs)) + "\n")

#writer.write((str(Comp_GM)) + "\n")
writer.write((str(Comp_Supervision)) + "\n")
writer.write((str(Comp_Salaries_Clerical)) + "\n")
writer.write((str(Comp_Other)) + "\n\n")


writer.write(str(Total_Sales_Comp) + "\n\n\n")


##########service##################

writer.write("\n\n###################################Service###################################### " "\n\n")

writer.write((str(Serv_Cus_Pay)) + "\n")
writer.write((str(Serv_Warr)) + "\n")
writer.write((str(Serv_Internal)) + "\n\n")

writer.write((str(Serv_Cus_Pay+Serv_Warr+Serv_Internal)) + "\n\n")

writer.write((str(Serv_Sublet)) + "\n\n")

writer.write((str(Serv_Cus_Pay+Serv_Warr+Serv_Internal+Serv_Sublet)) + "\n\n")

writer.write((str(Gross_Serv_Cus_Pay)) + "\n")
writer.write((str(Gross_Serv_Warr)) + "\n")
writer.write((str(Gross_Serv_Internal)) + "\n")
writer.write((str(Gross_Serv_Unapplied)) + "\n\n")

writer.write((str(Gross_Serv_Cus_Pay + Gross_Serv_Warr + Gross_Serv_Internal + Gross_Serv_Unapplied)) + "\n\n")

writer.write((str(Gross_Serv_Sublet)) + "\n\n")

writer.write((str(Gross_Serv_Cus_Pay + Gross_Serv_Warr + Gross_Serv_Internal + Gross_Serv_Unapplied+Gross_Serv_Sublet)) + "\n\n")

writer.write((str(Service_Variable)) + "\n")
writer.write((str(Service_Personnel)) + "\n")
writer.write((str(Service_Semi)) + "\n")
writer.write((str(Service_Fixed)) + "\n\n")

writer.write(str(Service_Variable + Service_Personnel + Service_Semi + Service_Fixed) + "\n\n")

writer.write(str((Gross_Serv_Cus_Pay + Gross_Serv_Warr + Gross_Serv_Internal + Gross_Serv_Unapplied+Gross_Serv_Sublet)-
                 (Service_Variable + Service_Personnel + Service_Semi + Service_Fixed)) + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

writer.write((str(Serv_Comp_Draws)) + "\n")
writer.write((str(Serv_Comp_Sales)) + "\n")
writer.write((str(Serv_Comp_Spiffs)) + "\n")
#writer.write((str(Serv_Comp_GM)) + "\n")
writer.write((str(Serv_Comp_Supervision)) + "\n")
writer.write((str(Serv_Comp_Salaries_Clerical)) + "\n")
writer.write((str(Serv_Comp_Other)) + "\n\n")


writer.write(str(Total_Serv_Comp) + "\n\n\n")

#############express###################################

writer.write("\n\n###################################Express###################################### " "\n\n")

writer.write((str(Express_Cus_Pay)) + "\n")
writer.write((str(Express_Warr)) + "\n")
writer.write((str(Express_Internal)) + "\n\n")

writer.write((str(Express_Cus_Pay+Express_Warr+Express_Internal)) + "\n\n")

writer.write(str(0) + "\n\n")

writer.write((str(Express_Cus_Pay+Express_Warr+Express_Internal)) + "\n\n")

writer.write((str(Gross_Express_Cus_Pay)) + "\n")
writer.write((str(Gross_Express_Warr)) + "\n")
writer.write((str(Gross_Express_Internal)) + "\n")
writer.write(str(0) + "\n\n")

writer.write(str(Gross_Express_Cus_Pay + Gross_Express_Warr + Gross_Express_Internal) + "\n\n")

writer.write(str(0) + "\n\n")

writer.write(str(Gross_Express_Cus_Pay + Gross_Express_Warr + Gross_Express_Internal) + "\n\n")



writer.write((str(Express_Variable)) + "\n")
writer.write((str(Express_Personnel)) + "\n")
writer.write((str(Express_Semi)) + "\n")
writer.write((str(Express_Fixed)) + "\n\n")

writer.write((str(Express_Variable+Express_Personnel+Express_Semi+Express_Fixed)) + "\n\n")

writer.write((str((Gross_Express_Cus_Pay + Gross_Express_Warr + Gross_Express_Internal)-
                  (Express_Variable+Express_Personnel+Express_Semi+Express_Fixed))) + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

writer.write((str(Express_Comp_Draws)) + "\n")
writer.write((str(Express_Comp_Sales)) + "\n")
writer.write((str(Express_Comp_Spiffs)) + "\n")
#writer.write((str(Express_Comp_GM)) + "\n")
writer.write((str(Express_Comp_Supervision)) + "\n")
writer.write((str(Express_Comp_Salaries_Clerical)) + "\n")
writer.write((str(Express_Comp_Other)) + "\n\n")


writer.write(str(Total_Express_Comp) + "\n\n\n")

####################BodyShop############################################

writer.write("\n\n###################################BodyShop###################################### " "\n\n")

writer.write((str(BodyShop_Cus_Pay)) + "\n")
writer.write((str(BodyShop_Warr)) + "\n")
writer.write((str(BodyShop_Internal)) + "\n\n")

writer.write(str(BodyShop_Cus_Pay + BodyShop_Warr + BodyShop_Internal) + "\n\n")

writer.write((str(BodyShop_Sublet)) + "\n")
writer.write((str(BodyShop_Materials)) + "\n\n")

writer.write((str(BodyShop_Cus_Pay + BodyShop_Warr + BodyShop_Internal+BodyShop_Sublet+BodyShop_Materials) + "\n\n"))

writer.write((str(Gross_BodyShop_Cus_Pay)) + "\n")
writer.write((str(Gross_BodyShop_Warr)) + "\n")
writer.write((str(Gross_BodyShop_Internal)) + "\n")
writer.write((str(Gross_BodyShop_Unapplied)) + "\n\n")

writer.write((str(Gross_BodyShop_Cus_Pay+Gross_BodyShop_Warr+Gross_BodyShop_Internal+Gross_BodyShop_Unapplied)) + "\n\n")

writer.write((str(Gross_BodyShop_Sublet)) + "\n")
writer.write((str(Gross_BodyShop_Materials)) + "\n\n")

writer.write((str(Gross_BodyShop_Cus_Pay + Gross_BodyShop_Warr + Gross_BodyShop_Internal +
                  Gross_BodyShop_Unapplied + Gross_BodyShop_Sublet + 
                  Gross_BodyShop_Materials) + "\n\n"))

writer.write((str(BodyShop_Variable)) + "\n")
writer.write((str(BodyShop_Personnel)) + "\n")
writer.write((str(BodyShop_Semi)) + "\n")
writer.write((str(BodyShop_Fixed)) + "\n\n")


writer.write((str(BodyShop_Variable+BodyShop_Personnel+BodyShop_Semi+BodyShop_Fixed)) + "\n\n")

writer.write((str((Gross_BodyShop_Cus_Pay + Gross_BodyShop_Warr + Gross_BodyShop_Internal + Gross_BodyShop_Unapplied + 
                   Gross_BodyShop_Sublet + Gross_BodyShop_Materials)-(BodyShop_Variable+BodyShop_Personnel+BodyShop_Semi+BodyShop_Fixed)) + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n"))

writer.write((str(BodyShop_Comp_Draws)) + "\n")
writer.write((str(BodyShop_Comp_Sales)) + "\n")
writer.write((str(BodyShop_Comp_Spiffs)) + "\n")
#writer.write((str(BodyShop_Comp_GM)) + "\n")
writer.write((str(BodyShop_Comp_Supervision)) + "\n")
writer.write((str(BodyShop_Comp_Salaries_Clerical)) + "\n")
writer.write((str(BodyShop_Comp_Other)) + "\n\n")


writer.write(str(Total_BodyShop_Comp) + "\n\n\n")

#########################Parts###############################################

writer.write("\n\n###################################Parts###################################### " "\n\n")

writer.write((str(Parts_Cus_Pay)) + "\n")
writer.write((str(Parts_Express)) + "\n")
writer.write((str(Parts_BodyShop)) + "\n")
writer.write((str(Parts_Warranty)) + "\n")
writer.write((str(Parts_Internal)) + "\n\n")

writer.write((str(Parts_Cus_Pay+Parts_Express+Parts_BodyShop+Parts_Warranty + Parts_Internal)) + "\n\n")

writer.write((str(Parts_Counter)) + "\n")
writer.write((str(Parts_Wholesale)) + "\n")
writer.write((str(Parts_Tires)) + "\n")
writer.write((str(Parts_Gas)) + "\n\n")

writer.write((str(Parts_Cus_Pay+Parts_Express+Parts_BodyShop+Parts_Warranty +
                  Parts_Internal+Parts_Counter+Parts_Wholesale + Parts_Tires + Parts_Gas)) + "\n\n")



writer.write((str(Gross_Parts_Cus_Pay)) + "\n")
writer.write((str(Gross_Parts_Express)) + "\n")
writer.write((str(Gross_Parts_BodyShop)) + "\n")
writer.write((str(Gross_Parts_Warr)) + "\n")
writer.write((str(Gross_Parts_Internal)) + "\n\n")

writer.write((str(Gross_Parts_Cus_Pay+Gross_Parts_Express+Gross_Parts_BodyShop+Gross_Parts_Internal + Gross_Parts_Warr
                  )) + "\n\n")

writer.write((str(Gross_Parts_Counter)) + "\n")
writer.write((str(Gross_Parts_Wholesale)) + "\n")
writer.write((str(Gross_Parts_Tires)) + "\n")
writer.write((str(Gross_Parts_Gas)) + "\n")
writer.write((str(Gross_Parts_Allowance)) + "\n")
writer.write((str(Gross_Parts_Disc)) + "\n\n")

writer.write((str(Gross_Parts_Cus_Pay+Gross_Parts_Express+Gross_Parts_BodyShop+Gross_Parts_Internal+Gross_Parts_Warr
                  +Gross_Parts_Counter+Gross_Parts_Wholesale+Gross_Parts_Tires+ Gross_Parts_Gas
                  +Gross_Parts_Allowance+Gross_Parts_Disc)) + "\n\n")


writer.write((str(Parts_Variable)) + "\n")
writer.write((str(Parts_Personnel)) + "\n")
writer.write((str(Parts_Semi)) + "\n")
writer.write((str(Parts_Fixed)) + "\n\n")

writer.write((str(Parts_Variable+Parts_Personnel+Parts_Semi+Parts_Fixed)) + "\n\n")

writer.write((str((Gross_Parts_Cus_Pay+Gross_Parts_Express+Gross_Parts_BodyShop+Gross_Parts_Internal+Gross_Parts_Warr
                  +Gross_Parts_Counter+Gross_Parts_Wholesale+Gross_Parts_Tires+ Gross_Parts_Gas
                  +Gross_Parts_Allowance+Gross_Parts_Disc) - 
                  (Parts_Variable+Parts_Personnel+Parts_Semi+Parts_Fixed))) + "\n\n\n\n\n\n\n\n\n\n\n\n\n")


writer.write((str(Parts_Comp_Draws)) + "\n")
writer.write((str(Parts_Comp_Sales)) + "\n")
writer.write((str(Parts_Comp_Spiffs)) + "\n")
#writer.write((str(Parts_Comp_GM)) + "\n")
writer.write((str(Parts_Comp_Supervision)) + "\n")
writer.write((str(Parts_Comp_Salaries_Clerical)) + "\n")
writer.write((str(Parts_Comp_Other)) + "\n\n")


writer.write(str(Total_Parts_Comp) + "\n\n\n")
####################################80-90################

writer.write("\n\n###################################81,82,91###################################### " "\n\n")

writer.write((str(Other_Income)) + "\n")
writer.write((str(Dealer_Fees)) + "\n")





