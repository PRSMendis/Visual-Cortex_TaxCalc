import collections
import bisect
from simple_term_menu import TerminalMenu


# initializing dictionary
tax_dict = collections.OrderedDict()
tax_dict = {2017: 'Hi', 2018: 'Hello',  2019: 'Gfg'}
str_map = {"2020-21": 2020, "2021-22": 2021}


def main():
    print("Please select the income year from the following: ")

    # Choose the tax year range from options, and map to int value

    options = ["2020-21", "2021-22"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {str_map[options[menu_entry_index]]}!")


    # res = bisect.bisect_left(list(tax_dict.keys()), 15.6)
if __name__ == "__main__":
    main()
