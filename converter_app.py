import csv

from flask import Flask, render_template, request

import csv_from_api

app = Flask(__name__)
csv_from_api.create_csv()


@app.route("/", methods=["GET", "POST"])
def form_view():
    currencies, content = [], " "
    with open("test.csv", newline="") as f:
        currencies_data = csv.DictReader(f, delimiter=';')
        for row in currencies_data:
            currencies.append(row["currency"])

    if request.method == 'POST':
        amount_pln = request.form['amount']
        currency = request.form['currencies']
        if not amount_pln.isdecimal():
            amount_pln = 0
        else:
            amount_pln = float(amount_pln)
        with open("test.csv", newline="") as f:
            currencies_data = csv.DictReader(f, delimiter=';')

            for row in currencies_data:
                if row.get("currency") == currency:
                    short = row.get("code")
                    bid = float(row.get("bid"))
                    result = amount_pln / bid
                    content = f'{amount_pln} PLN = {result:.2f} {short}'

    return render_template('/form_currency_converter.html', currencies=currencies, content=content)


if __name__ == '__main__':
    app.run(debug=True)
