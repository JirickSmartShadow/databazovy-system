from pohledyDAO import *
from lib.data_formatting import *


def get_all_prehled_filmu():
    rows = select_all_prehled_filmu()
    output = format_data(rows)
    return output


def get_all_prehled_promitani():
    rows = select_all_prehled_promitani()
    output = format_data(rows)
    return output


def get_all_celkovy_promitaci_cas():
    rows = select_all_celkovy_promitaci_cas()
    output = format_data(rows)
    return output
