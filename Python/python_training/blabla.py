import csv
with open('file.csv', newline='') as f:
   # reader=csv.reader(f,delimiter=':',quoting=csv.QUOTE_NONE)
    reader=csv.DictReader(f)
    for row in reader:
        #print(row)
        print(row['first_name'],row['last_name'])
    print(row)