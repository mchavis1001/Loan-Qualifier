# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.qualifier.utils.fileio import save_csv, load_csv

# Import Calculators
from qualifier.qualifier.utils import calculators

# Import Filters
from qualifier.qualifier.filters import credit_score
from qualifier.qualifier.filters import debt_to_income
from qualifier.qualifier.filters import loan_to_value
from qualifier.qualifier.filters import max_loan_size


def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    path = Path('./data/output/qualifying_loans.csv')
    data = [['testing', 123, 'test'], [123, 'test', 'testing'], ['test', 'testing', 123]]
    assert save_csv(path, data)


def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375


def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84


def test_filters():
    bank_data = load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!


if __name__ == "__main__":
    try:
        test_save_csv()
        print("Everything passed")
    except AssertionError as error:
        print(error)
