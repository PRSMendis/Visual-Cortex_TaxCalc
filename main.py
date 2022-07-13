import collections
import bisect
from simple_term_menu import TerminalMenu


# initializing dictionary
tax_dict = collections.OrderedDict()
# tax_dict = {2020: 'Hi', 2021: 'Hello'}
tax_dict = {2020:  {
    0: 1,
    18201: 2,
    45001: 3,
    120001: 4,
    180001: 5
}}
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

    res = bisect.bisect_left(
        list(tax_dict[str_map[options[menu_entry_index]]].keys()), income)

    print(res)

    # sorted(list_of_numbers, key=lambda x: abs(x - number))[0]
if __name__ == "__main__":
    main()
