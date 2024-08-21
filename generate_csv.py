import csv
import random
import datetime


def generate_csv(file_name, num_records):
    first_names = ["Evan", "Brian", "Sang", "Mike", "Erik"]
    last_names = ["Mesa", "Yee", "Nam", "Sok", "Milder"]
    addresses = ["123 East", "456 West", "789 North", "101 South", "202 East West"]

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["first_name", "last_name", "address", "date_of_birth"])

        for _ in range(num_records):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            address = random.choice(addresses)
            date_of_birth = datetime.date(1980, 1, 1) + datetime.timedelta(days=random.randint(0, 10000))
            writer.writerow([first_name, last_name, address, date_of_birth])

if __name__ == "__main__":
    generate_csv('data.csv', 1000000)