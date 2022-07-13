import csv
from pathlib import Path

## this function retrieves the filtered list of qualifying loans as Arg[0],
## and the user-retrieved file path to save this filtered loan list as Arg[1]
def save_csv(qualifying_loans, save_path):

    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]

    csvpath = Path(save_path)
    with open(csvpath, 'w') as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(header)

        for row in qualifying_loans:
            
            csvwriter.writerow(row)