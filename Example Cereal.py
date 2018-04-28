#Dependencies
import os
import csv

cereal_csv_path = os.path.join("Resources", "cereal.csv")


#Open and read csv
with open(cereal_csv_path, newline="")as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    #iterate through each row
    for row in csvreader:

    # Convert row to float and compare to grams of fiber
        if float(row[7]) >= 5:
            print(row)


