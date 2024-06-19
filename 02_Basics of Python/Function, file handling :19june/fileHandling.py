# File: A storage space where you can save data on permanent basis
# How data can be persisted in Python-> File handling
# Types-> .csv(comma delimited file), .xls or .xlsx file(Excel), .json(object file)

'''
.csv files
2 ways of working with csv file:
1.CSV module
2. Pandas module
'''

# csv module
import csv

# Create a sample file ans use it for writing
# a file can have in general 2 modes-> 'w' and 'r'
with open('firstFile.csv','w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["EmpID", "EmpName", "Salary", "Department"])
    writer.writerow([101,"Samar",10000,"Mkt"])
    writer.writerow([102,"Reema",15000,"Prod"])
    writer.writerow([103,"Raman",20000,"Mkt"])

data_list=[
    ["EmpID", "EmpName", "Salary", "Department"],
    [101,"Samar",10000,"Mkt"],
    [102,"Reema",15000,"Prod"],
    [103,"Raman",20000,"Mkt"]
]
with open('secondFile.csv','w',newline='') as file:
    writer=csv.writer(file, delimiter='|')
    writer.writerows(data_list)

with open('thirdFile.csv','w',newline='') as file:
    writer=csv.writer(file, delimiter=':',quotechar='*', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data_list)

with open('fourthFile.csv','w',newline='') as file:
    writer=csv.writer(file, delimiter='"',quotechar='*', quoting=csv.QUOTE_ALL)
    writer.writerows(data_list)

# To create a read-only file
with open('thirdFile.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

with open('thirdFile.csv','r') as file:
    reader=csv.reader(file,delimiter=':', skipinitialspace=True)
    for row in reader:
        print(row)

with open('fifthFile.csv','a',newline='') as file:
    writer=csv.writer(file, delimiter='|',quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerows(data_list)

with open('sixthFile.csv','w+',newline='') as file:
    writer=csv.writer(file, delimiter='|',quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerows(data_list)