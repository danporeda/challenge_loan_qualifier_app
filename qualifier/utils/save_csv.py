import csv
from pathlib import Path

def save_csv(qualifying_loans):

    headerpath = Path("data/daily_rate_sheet.csv")
    with open(headerpath, 'r') as headerfile:
    
        csvreader = csv.reader(headerfile)

        data =[]

        for row in csvreader:
            data.append(row)

    header = data[0][0:]

    csvpath = Path("data/qualifying_loans.csv")
    with open(csvpath, 'w') as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(header)

        for row in qualifying_loans:
            
            csvwriter.writerow(row)