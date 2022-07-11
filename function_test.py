import csv
from pathlib import Path

headerpath = Path("data/daily_rate_sheet.csv")
with open(headerpath, 'r') as headerfile:
    # headerreader = csv.reader(headerfile)

    header = next(headerfile)

    print(header)