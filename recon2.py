import csv


#####################read file######################################
#file_name = input('Enter file name: ')#then change all files to file_name
#with open('#DIZ8.csv', mode = 'r') as infile:

#def duplicates(value):
        

with open('# 5 3-21.csv', 'r', encoding = 'utf-8-sig') as infile:
    
    reader = csv.reader(infile)#read in specified file
    
    
###################################################################

    #want to negate statement so that values match
    """     
    convert column values to float and negate
    for column in reader:
        for cell in column[3]:
            #if (column[3] != ''):
            column[3] = float(column[3])
            column[3] = column[3]*-1
            break
        for cell in column[1]:
            #if (column[1] != ''):
            column[1] = float(column[1])
    """
  
    
    
    #create a set/dictionary. Column 0 is reference from schedule
    #while column 1 is amount from the schedule
    Schedule = {((column[0]), (column[1])): 'Schedule' for column in reader}
    
    #reopen for setting second dictionary 
           
    with open('# 5 3-21.csv', 'r', encoding = 'utf-8-sig') as infile:   
        reader = csv.reader(infile)
            
       
        Statement = {((column[2]), (column[3])): 'Statement' for column in reader}
        
                
######################write files#######################################################                
        
        writer = open("# 5 output 3-21.txt", "w")
        writer2 = open("# 5 output2 3-21.txt", "w")
        writer3 = open("# 5 values 3-21.txt", "w")
        """
        with open('# 5 3-21.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter = csvwriter.writerows(Statement)
            csvwriter = csvwriter.writerows(Schedule)
            """  
            
################################################################################        
        
       
        
        """check for duplicates????????
        duplicates = defaultdict(list)
        
        for k,v in Schedule:
            duplicates[k].append(v)
        for key, value in duplicates.items():
            if len(value) > 1:
                print(str(value))
        """
        
        #for each element in the schedule (reference and amount), check if 
        #these are exactly equal on the Statement
        
        for match in Schedule:
            
            
            if match not in Statement: 
                               
                
                match = map(str, match)#convert items in match to strings
                match = ','.join(match)#join items together with commas
                writer.write(str(match) + "\n")
                #csvwriter.writerows(str(match) + "\n")
                
        #Schedule_total = sum(Schedule.keys())
        
        #Now check if each element (reference and amount)
        #in statement matches schedule                       
        for match2 in Statement: 
            if match2 not in Schedule:
                
                match2 = map(str, match2)#convert items in match to strings
                match2 = ','.join(match2)#join items together with commas
                writer2.write(str(match2) + "\n")
                #csvwriter.writerows(str(match2) + "\n")
#########################only value match check code###############################                
"""         
        with open('#DIZ8.csv', 'r', encoding = 'utf-8-sig') as infile:   
            reader = csv.reader(infile)

          
            Values = {column[1]:'Schedule' for column in reader}
      
        
            with open('#DIZ.csv', mode = 'r') as infile:
                reader = csv.reader(infile)
                
                Values2 = {column[3]: 'Statement' for column in reader}
                    
                #writer2.write("\nNow checking values\n")
                for value_match in Values:
                    if value_match not in Values2:
                        #writer3.write(str(value_match) + "," + "Yes")
                    #else:
                        writer3.write(str(value_match).strip("(', ')") + "\n")
                
                for value_match2 in Values2:
                    if value_match2 not in Values:
                         #writer3.write(str(value_match2) + "," + "Yes")
                    #else:
                        writer3.write(str(value_match2).strip("(', ')")+"\n")
"""
                           
writer.close()
writer2.close()
#writer3.close()
    
                            
                            
                            