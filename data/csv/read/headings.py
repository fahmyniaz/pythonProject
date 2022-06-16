import csv

file_path = "../songs.csv"

with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)

        headings = next(csv_reader)

        for record in csv_reader:
            print(record)