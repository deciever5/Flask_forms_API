import requests
import csv


def create_csv():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    csv_columns = ["currency", "code", "bid", "ask"]
    with open("test.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns, delimiter=';')
        writer.writeheader()
        for line in data[0].get('rates'):
            writer.writerow(line)
