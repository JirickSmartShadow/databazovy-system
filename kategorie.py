from kategorieDAO import *
from lib.data_formatting import *


def get_all_kategorie():
    rows = select_all_kategorie()
    output = format_data(rows)
    return output


def get_kategorie_row_count():
    row_count = select_kategorie_row_count()
    return row_count
