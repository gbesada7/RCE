#import csv
import pandas as pd
#import numpy as np
#store 3

df = pd.read_csv('#3 2021-2.csv', usecols = ['Account', 'Desc', 'BalanceFwd', 'CurrMth', 'YTDBal', 'GroupType', 'SubType'])


####sales tab###################
Bfwd_total = df['BalanceFwd'].sum()

New_Sales_Total = df.loc[df.GroupType.isin(['110']), 'CurrMth'].sum()*-1
Used_Sales_Total = df.loc[df.GroupType.isin(['120']), 'CurrMth'].sum()*-1

Gross_New = df.loc[df.SubType.isin(['111', '211',]), 'CurrMth'].sum()*-1
Gross_New_FI = df.loc[df.SubType.isin(['114', '214']), 'CurrMth'].sum()*-1
Op_Support = df.loc[df.SubType.isin(['88',]), 'CurrMth'].sum()*-1

Gross_Used = df.loc[df.SubType.isin(['121', '221']), 'CurrMth'].sum()*-1
Gross_Used_FI = df.loc[df.SubType.isin(['124', '224']), 'CurrMth'].sum()*-1
Gross_Wholesale = df.loc[df.SubType.isin(['126', '226']), 'CurrMth'].sum()*-1

Sales_Variable= df.loc[df.Account.isin(['3013A','3014A','3015A','3019A','3056A','3057A','3058A','3059A','3013B',
                                        '3014B','3015B','3019B','3056B','3057B','3058B','3059B',]), 'CurrMth'].sum()
Sales_Personnel = df.loc[df.Account.isin(['3010A','3011A','3012A','3016A','3017A','3018A','3020A','3021A',
                                          '3022A','3023A','3024A','3025A','3026A','3027A','3028A','3029A',
                                          '3030A', '3010B','3011B','3012B','3016B','3017B','3018B','3020B','3021B',
                                          '3022B','3023B','3024B','3025B','3026B','3027B','3028B','3029B','3030B', '3039A', '3039B']), 'CurrMth'].sum()
Sales_Semi = df.loc[df.Account.isin(['3031A','3032A','3034A','3035A','3036A','3037A','3038A','3040A','3041A',
                                     '3042A','3043A','3044A','3045A','3046A','3047A','3048A','3049A','3051A',
                                     '3052A','3053A','3054A','3055A','3060A','3061A','3062A','3063A','3064A',
                                     '3066A','3068A','3070A','3071A','3072A','3073A','3074A','3075A','3076A',
                                     '3078A', '3031B','3032B','3034B','3035B','3036B','3037B','3038B','3040B',
                                     '3041B','3042B','3043B','3044B','3045B','3046B','3047B','3048B',
                                     '3049B','3051B','3052B','3053B','3054B','3055B','3060B','3061B',
                                     '3062B','3063B','3064B','3066B','3068B','3070B','3071B','3072B',
                                     '3073B','3074B','3075B','3076B','3078B',]), 'CurrMth'].sum()
Sales_Fixed = df.loc[df.Account.isin(['3080A','3081A','3082A','3084A','3085A','3086A','3087A','3088A',
                                      '3089A','3090A','3091A','3092A','3080B','3081B','3082B','3084B',
                                      '3085B','3086B','3087B','3088B','3089B','3090B','3091B','3092B', 
                                      '3083A','3083B',]), 'CurrMth'].sum()



Comp_Draws = df.loc[df.Account.isin(['3010A', '3010B']), 'CurrMth'].sum()
#Comp_RCE = df.loc[df.SubType.isin(['20F']), 'CurrMth'].sum()
Comp_Sales = df.loc[df.Account.isin(['3011A', '3011B']), 'CurrMth'].sum()
Comp_Spiffs = df.loc[df.Account.isin(['3017A', '3017B']), 'CurrMth'].sum() 
#Comp_GM = df.loc[df.Account.isin(['3020A', '3020B']), 'CurrMth'].sum()
Comp_Supervision = df.loc[df.Account.isin(['3021A', '3021B']), 'CurrMth'].sum()
Comp_Salaries_Clerical = df.loc[df.Account.isin(['3022A', '3022B']), 'CurrMth'].sum()
Comp_Other = df.loc[df.Account.isin(['3023A', '3023B']), 'CurrMth'].sum()

Comp_FI = df.loc[df.Account.isin(['3012A', '3012B']), 'CurrMth'].sum()

Total_Sales_Comp = (Comp_Draws + Comp_Sales + Comp_Spiffs + Comp_Supervision + Comp_Salaries_Clerical
                    + Comp_Other + Comp_FI)

#####service###############

Serv_Cus_Pay = df.loc[df.Account.isin(['3460','3460A','S460','3460E',]), 'CurrMth'].sum()*-1
Serv_Warr = df.loc[df.Account.isin(['3462','S462','3463P', 'S463P',]), 'CurrMth'].sum()*-1
Serv_Internal = df.loc[df.Account.isin(['3463','3463D','S463','S463D',]), 'CurrMth'].sum()*-1
Serv_Sublet = df.loc[df.Account.isin(['3466', 'S466']), 'CurrMth'].sum()*-1


Gross_Serv_Cus_Pay = df.loc[df.Account.isin(['3460','3460A','S460','3660','S660','3460E','3660E',]), 'CurrMth'].sum()*-1
Gross_Serv_Warr = df.loc[df.Account.isin(['3462','S462','3662','S662', '3463P','S463P','3663P','S663P',]), 'CurrMth'].sum()*-1
Gross_Serv_Internal = df.loc[df.Account.isin(['3463','3463D','S463','S463D','3663', '3663A', '3663D','S663','S663D',]), 'CurrMth'].sum()*-1
Gross_Serv_Sublet = df.loc[df.Account.isin(['3466','S466','3666','S666',]), 'CurrMth'].sum()*-1
Gross_Serv_Unapplied = df.loc[df.Account.isin(['3665']), 'CurrMth'].sum()*-1




Service_Variable = df.loc[df.Account.isin(['3013D','3014D','3015D','3019D','3056D','3057D','3058D','3059D',]), 'CurrMth'].sum()
Service_Personnel = df.loc[df.Account.isin(['3010D','3011D','3012D','3016D','3017D','3018D',
                                            '3020D','3021D','3022D','3023D','3024D','3025D','3026D',
                                            '3027D','3028D','3029D','3030D', '3039D']), 'CurrMth'].sum()
Service_Semi = df.loc[df.Account.isin(['3031D','3032D','3034D','3035D','3036D','3037D','3038D','3040D',
                                       '3041D','3042D','3043D','3044D','3045D','3046D','3047D','3048D',
                                       '3049D','3051D','3052D','3053D','3054D','3055D','3060D','3061D',
                                       '3062D','3063D','3064D','3066D','3068D','3070D','3071D','3072D',
                                       '3073D','3074D','3075D','3076D','3078D',]), 'CurrMth'].sum()
Service_Fixed = df.loc[df.Account.isin(['3080D','3081D','3082D','3084D','3085D','3086D',
                                        '3087D','3088D','3089D','3090D','3091D','3092D','3083D',]), 'CurrMth'].sum()

Serv_Comp_Draws = df.loc[df.Account.isin(['3010D']), 'CurrMth'].sum()
#Comp_RCE = df.loc[df.SubType.isin(['20F']), 'CurrMth'].sum()
Serv_Comp_Sales = df.loc[df.Account.isin(['3011D',]), 'CurrMth'].sum()
Serv_Comp_Spiffs = df.loc[df.Account.isin(['3017D',]), 'CurrMth'].sum() 
#Serv_Comp_GM = df.loc[df.Account.isin(['3020D']), 'CurrMth'].sum()
Serv_Comp_Supervision = df.loc[df.Account.isin(['3021D',]), 'CurrMth'].sum()
Serv_Comp_Salaries_Clerical = df.loc[df.Account.isin(['3022D',]), 'CurrMth'].sum()
Serv_Comp_Other = df.loc[df.Account.isin(['3023D']), 'CurrMth'].sum()



Total_Serv_Comp = (Serv_Comp_Draws + Serv_Comp_Sales + Serv_Comp_Spiffs + Serv_Comp_Supervision + 
                   Serv_Comp_Salaries_Clerical + Serv_Comp_Other)


#########Parts################################
Parts_Cus_Pay = df.loc[df.Account.isin(['3467','3467A', '3467E']), 'CurrMth'].sum()*-1
Parts_Warr = df.loc[df.Account.isin(['3480']), 'CurrMth'].sum()*-1
Parts_Internal = df.loc[df.Account.isin(['3481']), 'CurrMth'].sum()*-1
Parts_Counter = df.loc[df.Account.isin(['3482',]), 'CurrMth'].sum()*-1
Parts_Wholesale = df.loc[df.Account.isin(['3483',]), 'CurrMth'].sum()*-1
Parts_Gas = df.loc[df.Account.isin(['3491',]), 'CurrMth'].sum()*-1
Parts_Tires = df.loc[df.Account.isin(['3492',]), 'CurrMth'].sum()*-1

Gross_Parts_Cus_Pay = df.loc[df.Account.isin(['3467','3467A', '3467E', '3667', '3667E',]), 'CurrMth'].sum()*-1
Gross_Parts_Warr = df.loc[df.Account.isin(['3480', '3680',]), 'CurrMth'].sum()*-1
Gross_Parts_Internal = df.loc[df.Account.isin(['3481', '3681',]), 'CurrMth'].sum()*-1
Gross_Parts_Counter = df.loc[df.Account.isin(['3482', '3682',]), 'CurrMth'].sum()*-1
Gross_Parts_Wholesale = df.loc[df.Account.isin(['3483', '3683',]), 'CurrMth'].sum()*-1
Gross_Parts_Tires = df.loc[df.Account.isin(['3492', '3692']), 'CurrMth'].sum()*-1

Gross_Parts_Gas = df.loc[df.Account.isin(['3491', '3691']), 'CurrMth'].sum()*-1
Gross_Parts_Disc = df.loc[df.Account.isin(['3688']), 'CurrMth'].sum()*-1

Parts_Variable = df.loc[df.Account.isin(['3013F','3014F','3015F','3019F','3056F','3057F',
                                         '3058F','3059F',]), 'CurrMth'].sum()
Parts_Personnel = df.loc[df.Account.isin(['3010F','3011F','3012F','3016F','3017F','3018F',
                                          '3020F','3021F','3022F','3023F','3024F','3025F','3026F',
                                          '3027F','3028F','3029F','3030F',]), 'CurrMth'].sum()
Parts_Semi = df.loc[df.Account.isin(['3031F','3032F','3034F','3035F','3036F','3037F','3038F','3040F',
                                     '3041F','3042F','3043F','3044F','3045F','3046F','3047F','3048F',
                                     '3049F','3051F','3052F','3053F','3054F','3055F','3060F','3061F',
                                     '3062F','3063F','3064F','3066F','3068F','3070F','3071F','3072F',
                                     '3073F','3074F','3075F','3076F', '3077F', '3078F',]), 'CurrMth'].sum()
Parts_Fixed = df.loc[df.Account.isin(['3080F','3081F','3082F','3084F','3085F',
                                      '3086F','3087F','3088F','3089F','3090F','3091F','3092F', '3083F',]), 'CurrMth'].sum()

Parts_Comp_Draws = df.loc[df.Account.isin(['3010F']), 'CurrMth'].sum()
#Comp_RCE = df.loc[df.SubType.isin(['20F']), 'CurrMth'].sum()
Parts_Comp_Sales = df.loc[df.Account.isin(['3011F',]), 'CurrMth'].sum()
Parts_Comp_Spiffs = df.loc[df.Account.isin(['3017F',]), 'CurrMth'].sum() 
#Parts_Comp_GM = df.loc[df.Account.isin(['3020F']), 'CurrMth'].sum()
Parts_Comp_Supervision = df.loc[df.Account.isin(['3021F',]), 'CurrMth'].sum()
Parts_Comp_Salaries_Clerical = df.loc[df.Account.isin(['3022F',]), 'CurrMth'].sum()
Parts_Comp_Other = df.loc[df.Account.isin(['3023F']), 'CurrMth'].sum()



Total_Parts_Comp = (Parts_Comp_Draws + Parts_Comp_Sales + Parts_Comp_Spiffs + Parts_Comp_Supervision + 
                   Parts_Comp_Salaries_Clerical + Parts_Comp_Other)

########80-90#################

Other_Income = df.loc[df.Account.isin(['3900','3905','3905D','3905E','3905WG','3955','3955I',]), 'CurrMth'].sum()*-1
Dealer_Fees = df.loc[df.Account.isin(['3904']), 'CurrMth'].sum()*-1

#########################output########################

#######sales#########
writer = open("#3 numbers.txt", "w")
writer.write((str(New_Sales_Total)) + "\n")
writer.write((str(Used_Sales_Total)) + "\n\n")

writer.write((str(New_Sales_Total+Used_Sales_Total)) + "\n\n")

writer.write((str(Gross_New+Gross_New_FI+Op_Support)) + "\n")
writer.write((str(Gross_Used+Gross_Used_FI+Gross_Wholesale)) + "\n\n")

writer.write((str(Gross_New+Gross_New_FI+Op_Support+Gross_Used+Gross_Used_FI+Gross_Wholesale)) + "\n\n")

writer.write((str(Sales_Variable)) + "\n")
writer.write((str(Sales_Personnel)) + "\n")
writer.write((str(Sales_Semi)) + "\n")
writer.write((str(Sales_Fixed)) + "\n\n")

writer.write((str(Sales_Variable+Sales_Personnel+Sales_Semi+Sales_Fixed)) + "\n\n")

writer.write((str((Gross_New+Gross_New_FI+Gross_Used+Gross_Used_FI+Op_Support+Gross_Wholesale)
                  -(Sales_Variable+Sales_Personnel+Sales_Semi+Sales_Fixed))) + "\n\n\n\n")

writer.write((str(Gross_New)) + "\n")
writer.write((str(Gross_New_FI)) + "\n")
writer.write((str(Op_Support)) + "\n")
writer.write((str(Gross_New + Gross_New_FI + Op_Support)) + "\n\n\n")


writer.write((str(Gross_Used)) + "\n")
writer.write((str(Gross_Used_FI)) + "\n")
writer.write((str(Gross_Used+Gross_Used_FI)) + "\n\n")
writer.write((str(Gross_Wholesale)) + "\n")
writer.write(str(Gross_Used+Gross_Used_FI+Gross_Wholesale) + "\n\n")

writer.write(((str((Gross_New + Gross_New_FI+Op_Support) + (Gross_Used+Gross_Used_FI+Gross_Wholesale)) + "\n\n\n")))


writer.write((str(Op_Support)) + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

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

writer.write((str(Gross_Serv_Cus_Pay + Gross_Serv_Warr + Gross_Serv_Internal
                  + Gross_Serv_Unapplied + Gross_Serv_Sublet)) + "\n\n")

writer.write((str(Service_Variable)) + "\n")
writer.write((str(Service_Personnel)) + "\n")
writer.write((str(Service_Semi)) + "\n")
writer.write((str(Service_Fixed)) + "\n\n")

writer.write(str(Service_Variable + Service_Personnel + Service_Semi + Service_Fixed) + "\n\n")

writer.write(str((Gross_Serv_Cus_Pay + Gross_Serv_Warr + Gross_Serv_Internal + Gross_Serv_Unapplied + Gross_Serv_Sublet)-
                 (Service_Variable + Service_Personnel + Service_Semi + Service_Fixed)) + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

writer.write((str(Serv_Comp_Draws)) + "\n")
writer.write((str(Serv_Comp_Sales)) + "\n")
writer.write((str(Serv_Comp_Spiffs)) + "\n")
#writer.write((str(Serv_Comp_GM)) + "\n")
writer.write((str(Serv_Comp_Supervision)) + "\n")
writer.write((str(Serv_Comp_Salaries_Clerical)) + "\n")
writer.write((str(Serv_Comp_Other)) + "\n\n")


writer.write(str(Total_Serv_Comp) + "\n\n\n")

#########################Parts###############################################

writer.write("\n\n###################################Parts###################################### " "\n\n")

writer.write((str(Parts_Cus_Pay)) + "\n")
writer.write(str(0) + "\n")
writer.write(str(0) + "\n")
writer.write((str(Parts_Warr)) + "\n")
writer.write((str(Parts_Internal)) + "\n\n")

writer.write((str(Parts_Cus_Pay+Parts_Warr+Parts_Internal)) + "\n\n")

writer.write((str(Parts_Counter)) + "\n")
writer.write((str(Parts_Wholesale)) + "\n")
writer.write((str(Parts_Tires)) + "\n")
writer.write((str(Parts_Gas)) + "\n\n")


writer.write((str(Parts_Counter+Parts_Wholesale+Parts_Cus_Pay+Parts_Warr+Parts_Internal+Parts_Tires+Parts_Gas)) + "\n\n")

writer.write((str(Gross_Parts_Cus_Pay)) + "\n")
writer.write(str(0) + "\n")
writer.write(str(0) + "\n")
writer.write((str(Gross_Parts_Warr)) + "\n")
writer.write((str(Gross_Parts_Internal)) + "\n\n")

writer.write((str(Gross_Parts_Cus_Pay+Gross_Parts_Warr+Gross_Parts_Internal))+ "\n\n")

writer.write((str(Gross_Parts_Counter)) + "\n")
writer.write((str(Gross_Parts_Wholesale)) + "\n")
writer.write((str(Gross_Parts_Tires)) + "\n")
writer.write((str(Gross_Parts_Gas))+"\n")
writer.write((str(Gross_Parts_Disc)) + "\n")
writer.write((str(0)) + "\n\n")

writer.write((str(Gross_Parts_Cus_Pay+Gross_Parts_Warr+Gross_Parts_Internal+
               Gross_Parts_Counter+Gross_Parts_Wholesale+Gross_Parts_Disc + +Gross_Parts_Tires+Gross_Parts_Gas)) + "\n\n")

writer.write((str(Parts_Variable)) + "\n")
writer.write((str(Parts_Personnel)) + "\n")
writer.write((str(Parts_Semi)) + "\n")
writer.write((str(Parts_Fixed)) + "\n\n")

writer.write((str(Parts_Variable+Parts_Personnel+Parts_Semi+Parts_Fixed))+"\n\n")

writer.write(str((Gross_Parts_Cus_Pay+Gross_Parts_Warr+Gross_Parts_Internal+
               Gross_Parts_Counter+Gross_Parts_Wholesale+Gross_Parts_Disc + Gross_Parts_Gas + Gross_Parts_Tires)+
              -(Parts_Variable+Parts_Personnel+Parts_Semi+Parts_Fixed)) + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


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