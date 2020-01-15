import csv
with open('new.csv', mode='w') as csv_file:
    employee_write=csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    employee_write.writerow(['John Smith','Accounting','November'])
