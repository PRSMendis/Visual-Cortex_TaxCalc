import collections
import bisect
from simple_term_menu import TerminalMenu


# initializing dictionary
tax_dict = collections.OrderedDict()
# tax_dict = {2020: 'Hi', 2021: 'Hello'}

# Might need to bump up index vals up by 1 due to binary search
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
    }
}
str_map = {"2020-21": 2020, "2021-22": 2021}


def main():
    print("Please select the income year from the following: ")

    # Choose the tax year range from options, and map to int value

    options = ["2020-21", "2021-22"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {str_map[options[menu_entry_index]]}!")

    income: float = float(
        input("Please enter your total taxable income for the full income year::\n"))

    print(income)

    # Search through dict and find appropriate tax bracket key

    # idx = bisect.bisect_left(
    #     list(tax_dict[str_map[options[menu_entry_index]]].keys()), income)

    if income <= 18200:
        return 0

    income_dict = tax_dict[str_map[options[menu_entry_index]]]

    rates = income_dict.get(income) or income_dict[
        min(income_dict.keys(), key=lambda key: abs(key-income))]

    print("income_dict.keys()", income_dict.keys())
    print("min(income_dict.keys(), key=lambda key: abs(key-income))",
          min(income_dict.keys(), key=lambda key: key-income))

    print("res", rates)

    income_tax = rates["lump"] + \
        ((income - rates["threshold"]) * rates["rate"])

    print(income_tax)

    return income_tax

    # sorted(list_of_numbers, key=lambda x: abs(x - number))[0]
if __name__ == "__main__":
    main()
