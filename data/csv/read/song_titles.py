import csv

file_path = "../songs.csv"

with open(file_path) as file:
  csv_reader = csv.reader(file)
  headings = next(csv_reader)
  for values in csv_reader:
    # display only the names
    print(values[1])