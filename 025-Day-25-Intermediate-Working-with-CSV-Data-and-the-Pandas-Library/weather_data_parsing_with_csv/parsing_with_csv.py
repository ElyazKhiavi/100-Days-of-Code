import csv

with open("./weather_data.csv", "r") as f:
    data = csv.reader(f)
    temperature = []
    for row in data:
        print(row)
        # print(row)
        try:
            temperature.append(int(row[1]))
        except ValueError:
            print("Hit the header!")


print(temperature)
