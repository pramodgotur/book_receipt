from datetime import datetime, timedelta

BOOK_RENTS = {
    'regular': 1.5,
    'fiction': 3,
    'novel': 1.5
}


def get_total_rented_days(rented_on, returned_on):
    rented_on_date = datetime.strptime(rented_on, "%Y-%m-%d")
    returned_on_date = datetime.strptime(returned_on, "%Y-%m-%d")
    if returned_on_date < rented_on_date:
        return 0, False
    total_rented_days = (
        (returned_on_date-rented_on_date) + timedelta(days=1)).days
    return total_rented_days, True


def get_total_rent_in_rs(total_books_rented, total_rented_days, book_type):
    return total_books_rented * \
        total_rented_days * BOOK_RENTS[book_type]


def get_total_rent(request_form_data):
    book_wise_total_rent = {'regular': {"rented_days": 0, 'total_books': 0, 'rent_in_rs': 0},
                            'fiction': {"rented_days": 0, 'total_books': 0, 'rent_in_rs': 0},
                            'novel': {"rented_days": 0, 'total_books': 0, 'rent_in_rs': 0}}
    total_rent = 0
    for book_type in ('regular', 'fiction', 'novel'):
        rented_on, returned_on = request_form_data['rented-on-' +
                                                   book_type], request_form_data['returned-on-' + book_type]
        if rented_on and returned_on:
            total_books = int(
                request_form_data['total-' + book_type + '-rented'])
            rented_days, is_valid = get_total_rented_days(
                rented_on, returned_on)
            if not is_valid:
                return book_wise_total_rent, total_rent, is_valid, f"Invalid Book rent duration for {book_type} books"
            book_wise_total_rent[book_type]['total_books'] = total_books
            book_wise_total_rent[book_type]['rented_days'] = rented_days
            rent_in_rs = get_total_rent_in_rs(
                total_books, rented_days, book_type)
            book_wise_total_rent[book_type]['rent_in_rs'] = rent_in_rs
            total_rent += rent_in_rs
    return book_wise_total_rent, total_rent, True, ""
