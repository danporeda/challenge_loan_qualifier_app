## Loan Qualifier App

This Project retrieves user data and filters it through a list of bank loans to determine which loans they qualify for. User data is collected through CLI and includes credit score, monthly debt, monthly income, desired loan amount, and home value. This will streamline the user's mortgage application process by predetermining which loans they qualify for. 

---

## Technologies

This project is written in Python 3.7, and uses libraries and frameworks including `pathlib`, `csv`, `questionary`, and `fire`.

---

## Installation Guide
copy the link to the repository here: ```git@github.com:danporeda/challenge_loan_qualifier_app.git``` 

open Terminal(Mac) or gitBash, `cd` to the desired directory, and run: ```git clone git@github.com:danporeda/challenge_loan_qualifier_app.git```.

activate your `dev` environment: ```conda activate dev```.

run the program: `python app.py`.

---

## Usage

The program starts with a prompt asking for a file-path to a rate sheet. This file is included in the repository, type into the CLI: ```./data/daily_rate_sheet.csv```.  The CLI proceeds to ask for your credit score, monthly debt, monthly income, desired loan amount, and home value. The resulting output is a message of the amount of loans qualified for. Then the user is prompted with the option to save this list of qualifying loans; at this point, type "Y" or "N". If yes, then another prompt asks which file path you wish to save the qualifying loans to. 
![screen shot](https://github.com/danporeda/challenge_loan_qualifier_app/blob/7d1ecb761285a4a2a79c23cbb0affac37c6d59db/screen_shot_ex.png)

---

## Contributors

Brought to you by the talented folks at Denver University Fintech bootcamp, and yours truly, Dan Poreda. 

---

## License

Free for all. do whatever you want with it.
