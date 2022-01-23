from libs.submit import SubmitForm
from pathlib import Path
import csv

path_csv = Path(__file__).parent.joinpath('csv').joinpath('users.csv')


def create_csv(fieldnames: list) -> None:
    with open(path_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        writer.writerow({'id_user': '1', 'username': 'Liam'})
        writer.writerow({'id_user': '2', 'username': 'Noah'})
        writer.writerow({'id_user': '3', 'username': 'Olivia'})
        writer.writerow({'id_user': '4', 'username': 'Emma'})


# create_csv(['id_user', 'username'])
with open(path_csv, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        form = SubmitForm(row['id_user'], row['username'])
        form.submit()
