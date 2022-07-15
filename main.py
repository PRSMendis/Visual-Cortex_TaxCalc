import collections
from simple_term_menu import TerminalMenu
tax_dict = {
    2020:  {
        18201: {
            "lump": 0,
            "threshold": 18200,
            "rate": 0.19
        },
        45001: {
            "lump": 5092,
            "threshold": 45000,
            "rate": 0.325
        },
        120001: {
            "lump": 29467,
            "threshold": 120000,
            "rate": 0.37
        },
        180001: {
            "lump": 51667,
            "threshold": 180000,
            "rate": 0.45
        }
    },
    2021:  {
        18201: {
            "lump": 0,
            "threshold": 18200,
            "rate": 0.19
        },
        45001: {
            "lump": 5092,
            "threshold": 45000,
            "rate": 0.325
        },
        120001: {
            "lump": 29467,
            "threshold": 120000,
            "rate": 0.37
        },
        180001: {
            "lump": 51667,
            "threshold": 180000,
            "rate": 0.45
        }
    }
}

str_map = {"2020-21": 2020, "2021-22": 2021}

# python version 3.19.12


def user_input() -> float:
    while True:
        try:
            val = float(
                input("Please enter your total taxable income for the full income year:\n"))
            if val < 0:
                print("Sorry, input must be a positive value, try again")
                continue
            else:
                return val
        except ValueError:
            print("Input only accepts numbers.")


def calculator(income, year_dict):

    min_tax_threshold = min(year_dict.keys())

    if income < min_tax_threshold:
        print(f"The estimated tax on your taxable income is: $0")
    else:
        # access the year subcollection

        # access the rates that affect the user based on input number
        rates = year_dict.get(income) or year_dict[
            min([num for num in year_dict.keys() if num < income], key=lambda x: abs(x-income))]

        # calculate income tax
        income_tax = rates["lump"] + \
            ((income - rates["threshold"]) * rates["rate"])

        print(
            f"The estimated tax on your taxable income is: ${'{:,.2f}'.format(income_tax)}")

        # (potential optimisation) use binary search for larger dataset
        # idx = bisect.bisect_left(
        #     list(tax_dict[str_map[options[menu_entry_index]]].keys()), income)


def main(tax_dict, str_map):
    print("Please select the income year from the following: ")
    # Choose the tax year range from options, and map to float value

    options = ["2020-21", "2021-22"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    income = user_input()
    year_dict = tax_dict[str_map[options[menu_entry_index]]]
    calculator(income=income, year_dict=year_dict)


if __name__ == "__main__":
    main(tax_dict=tax_dict, str_map=str_map)
