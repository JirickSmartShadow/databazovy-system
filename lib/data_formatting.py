from tabulate import tabulate


def format_data(data):
    return tabulate(data[1:], headers=data[0], showindex=False, tablefmt='rounded_grid', missingval='unknown')
