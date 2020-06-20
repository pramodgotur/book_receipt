from flask import Flask, render_template, request, redirect
from rent_calculation_helper import get_total_rent


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    context = {"message": "", "messge_type": ""}
    if request.method == 'POST':
        book_wise_total_rent, total_rent, is_valid_dates, error_msg = get_total_rent(
            request.form)
        if not is_valid_dates:
            context["message"] = error_msg
            context["messge_type"] = "danger"
            return render_template("home.html", context=context)
        app.logger.warning(total_rent)
        context['book_wise_total_rent'] = book_wise_total_rent
        context['total_rent'] = total_rent
        return render_template("rent_receipt.html", context=context)
    return render_template("home.html", context=context)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
