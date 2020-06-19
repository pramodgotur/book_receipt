from flask import Flask, render_template, request, redirect
from rent_calculation_helper import get_total_rented_days, get_total_rent_in_rs


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    context = {"message": "", "messge_type": ""}
    if request.method == 'POST':
        total_books_rented = int(request.form['total-books-rented'])
        rented_on = request.form['rented-on']
        returned_on = request.form['returned-on']

        app.logger.info(request.form)

        total_rented_days, is_valid_dates = get_total_rented_days(
            rented_on, returned_on)
        if not is_valid_dates:
            context["message"] = "Invalid Book rent duration"
            context["messge_type"] = "danger"
            return render_template("home.html", context=context)
        total_rent_in_rs = get_total_rent_in_rs(
            total_books_rented, total_rented_days)

        context['total_rented_days'] = total_rented_days
        context['total_books_rented'] = total_books_rented
        context['total_rent_in_rs'] = total_rent_in_rs
        return render_template("rent_receipt.html", context=context)
    return render_template("home.html", context=context)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
