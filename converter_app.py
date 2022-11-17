import csv

from flask import Flask, render_template

import csv_from_api

app = Flask(__name__)
csv_from_api.create_csv()


@app.route("/", methods=["GET", "POST"])
def form_view():
    currencies=[]
    with open("test.csv",newline="") as f:
        currencies_data = csv.DictReader(f,delimiter=';')
        for row in currencies_data:
            currencies.append(row["currency"])
    return render_template('/form_currency_converter.html', currencies=currencies)


if __name__ == '__main__':
    app.run(debug=True)
