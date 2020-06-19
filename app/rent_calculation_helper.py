from datetime import datetime


def get_total_rented_days(rented_on, returned_on):
    rented_on_date = datetime.strptime(rented_on, "%Y-%m-%d")
    returned_on_date = datetime.strptime(returned_on, "%Y-%m-%d")
    if returned_on_date < rented_on_date:
        return 0, False
    total_rented_days = (returned_on_date-rented_on_date).days
    return total_rented_days, True


def get_total_rent_in_rs(total_books_rented, total_rented_days):
    total_rent_in_rs = total_books_rented * total_rented_days * 1
    return total_rent_in_rs
