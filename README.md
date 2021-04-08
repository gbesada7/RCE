# RCE
Rick case python automated programs mostly using pandas


#reconciliation (recon2.py)
Essentially I began with the first program automating reconciliation processes at RCE because they did not have quickbooks. 
Had help from cousins who are more advanced to create keys that would
compare both the value and reference number against the statement. Pretty tricky as keys do not support any duplicate values. If there are duplicates posted in excel the output 
could be incorrect. The reconciliation program (recon2) will read in a csv file that has the reference and amount on the stuff posted and the statement and output values
that do not completely match. 

##1FinReview, #3FinReview Financial presentation of monthly or Year to Date company performance
Used pandas to essentially do what I was doing before in excel which was filtering the columns and rows that were necessary to provide information such as sales revenue, 
gross revenue, expenses, net income...etc. Used past data to predict what rows needed to be filtered out and used account numbers in many situations. 
Program not 100% as account numbers may change monthly. 
The program will output a text file with which I was able to add the necessary spacing and copy and paste the data into the format that was already fixed in excel. Huge time saver
and also more accurate. 

#Fuel.py
Analysis of allocation of fuel expenses by company. See more information in file. Same process as Financial presentation.

#1 BS, #1 FinStatement  
Similar process to fin review but this is a summary of the income statement and balance sheet information. 
