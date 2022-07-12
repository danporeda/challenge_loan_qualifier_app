import csv
from pathlib import Path

headerpath = Path("data/daily_rate_sheet.csv")
with open(headerpath, 'r') as headerfile:
    
    csvreader = csv.reader(headerfile)

    data =[]

    for row in csvreader:
        data.append(row)

    header = data[0][0:]
    print(header)

csvpath = Path("function_test.csv")
with open(csvpath, 'w') as csvfile:

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)

# csvpath = Path("function_test.csv")
# with open(csvpath, 'w') as csvfile:

#     csvwriter = csv.writer(csvfile)

#     csvwriter.writerow([header])
# table_data = [
#     ['apple', 'kiwi', 'banana'],
#     ['football', 'baseball', 'hockey'],
#     ['jets', 'giants', 'bears']
# ]

# fruits = table_data[0]
# print(fruits)

# csvpath = Path("function_test.csv")
# with open(csvpath, 'w') as csvfile:

#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fruits)
